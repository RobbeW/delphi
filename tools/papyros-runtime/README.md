# Papyros frontend runtime bundle

Delphi serves `vendor/papyros/runtime.mjs` from its own origin. The bundle exports
Papyros 4.0.7, its shared BackendManager, sync-message's makeChannel and Comlink's
proxy together. This avoids UNPKG's transitive ESM redirects/CORS failures and
keeps the backend registry and callback markers in one dependency graph.

The generated assets are committed/deployed with the static site. Visitors and
local development servers do not need npm. The existing Python/JavaScript workers
and the platform's other CDN resources still need internet access.

To reproduce the bundle from the project root (Node.js 18+ and npm):

```sh
npm ci --ignore-scripts --prefix tools/papyros-runtime
npm run build --prefix tools/papyros-runtime
```

`package-lock.json` pins the complete dependency graph. The build rejects external
imports and creates the bundle, retained legal comments, complete contributing
package licences and a version/SHA-256 provenance manifest in `vendor/papyros/`.
Deploy that directory together with `app.js` and `platform.html`.

The frontend build uses pyodide-worker-runner's shipped TypeScript source so it
can retain PyodideClient without pulling its worker-only Pyodide loader into the
page. A loader handles the upstream raw Python text import. No Python runtime is
replaced: `papyros-python-worker.js` still loads its existing Pyodide version.

When updating the generated bundle, increment `APP_VERSION` in `app.js` and the
matching script query in `platform.html`. Verify runtime startup, Python output,
interactive input and exercise evaluation under `/delphi/`, with UNPKG blocked.
