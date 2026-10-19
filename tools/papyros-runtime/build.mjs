import { build } from "esbuild";
import { readFile, writeFile, mkdir } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { createHash } from "node:crypto";

const here = path.dirname(fileURLToPath(import.meta.url));
const output = path.resolve(here, "../../vendor/papyros");
await mkdir(output, { recursive: true });
const result = await build({
  absWorkingDir: here,
  entryPoints: ["entry.mjs"],
  outfile: path.join(output, "runtime.mjs"),
  bundle: true,
  format: "esm",
  platform: "browser",
  target: "es2022",
  minify: true,
  legalComments: "linked",
  metafile: true,
  plugins: [{
    name: "frontend-pyodide-client",
    setup(builder) {
      // The package's UMD entry eagerly requires the entire Pyodide runtime.
      // Its shipped ESM/TypeScript source lets us keep only PyodideClient;
      // Delphi's Python worker already owns Pyodide loading.
      builder.onResolve({ filter: /^pyodide-worker-runner$/ }, () => ({
        path: path.join(here, "node_modules/pyodide-worker-runner/lib/index.ts"),
      }));
      builder.onResolve({ filter: /^pyodide$/ }, () => ({
        path: "pyodide", external: true, sideEffects: false,
      }));
      builder.onResolve({ filter: /^!!raw-loader!/ }, ({ path: specifier, resolveDir }) => ({
        path: path.resolve(resolveDir, specifier.slice("!!raw-loader!".length)),
        namespace: "python-text",
      }));
      builder.onLoad({ filter: /.*/, namespace: "python-text" }, async ({ path: filename }) => ({
        contents: `export default ${JSON.stringify(await readFile(filename, "utf8"))};`,
        loader: "js",
      }));
    },
  }],
});

if (Object.values(result.metafile.outputs).some(file => file.imports.length)) {
  throw new Error("Frontend bundle must not retain external imports");
}

// Include complete licence files for every package contributing to the bundle.
const packages = new Map();
const contributingInputs = new Set(Object.values(result.metafile.outputs).flatMap(file =>
  Object.entries(file.inputs).filter(([, data]) => data.bytesInOutput > 0).map(([input]) => input)
));
for (const input of contributingInputs) {
  const match = input.replace(/^python-text:/, "").replaceAll("\\", "/").match(/^(.*node_modules\/((?:@[^/]+\/)?[^/]+))\//);
  if (match) packages.set(path.resolve(here, match[1]), match[2]);
}
const notices = [];
const dependencies = [];
for (const [directory, name] of [...packages].sort((a, b) => a[1].localeCompare(b[1], "en"))) {
  const packageRoot = path.resolve(here, directory);
  const info = JSON.parse(await readFile(path.join(packageRoot, "package.json"), "utf8"));
  let licence;
  for (const filename of ["LICENSE", "LICENSE.md", "LICENSE.txt", "license", "license.md", "license.txt", "LICENCE"]) {
    try {
      licence = await readFile(path.join(packageRoot, filename), "utf8");
      break;
    } catch (error) {
      if (error.code !== "ENOENT") throw error;
    }
  }
  if (!licence) throw new Error(`Missing licence file for ${name}`);
  notices.push(`===== ${name}@${info.version} (${info.license}) =====\n\n${licence.trim()}\n`);
  dependencies.push({ name, version: info.version, license: info.license });
}
await writeFile(path.join(output, "LICENSES.txt"), notices.join("\n"));
const bundle = await readFile(path.join(output, "runtime.mjs"));
await writeFile(path.join(output, "provenance.json"), JSON.stringify({
  description: "Papyros frontend state, shared BackendManager, sync-message and Comlink proxy; bundled from npm with tools/papyros-runtime/package-lock.json.",
  build: "npm ci --ignore-scripts --prefix tools/papyros-runtime && npm run build --prefix tools/papyros-runtime",
  esbuild: "0.25.12",
  sha256: createHash("sha256").update(bundle).digest("hex"),
  dependencies,
}, null, 2) + "\n");
console.log(`Built ${bundle.length} bytes with ${dependencies.length} dependency licences in vendor/papyros/`);
