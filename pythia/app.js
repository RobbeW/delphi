/* Copyright 2026 - Gebruik vrij voor educatie mits expliciete naamsvermelding */
"use strict";

const ui = {
  exerciseFolder: document.getElementById("exercise-folder"),
  exerciseTitleNl: document.getElementById("exercise-title-nl"),
  exerciseTitleEn: document.getElementById("exercise-title-en"),
  language: document.getElementById("language"),
  access: document.getElementById("access"),
  labels: document.getElementById("labels"),
  contact: document.getElementById("contact"),
  copyright: document.getElementById("copyright"),
  testSuite: document.getElementById("test-suite"),
  configPreview: document.getElementById("config-preview"),
  descriptionBody: document.getElementById("description-body"),
  testsBody: document.getElementById("tests-body"),
  tcStdin: document.getElementById("tc-stdin"),
  tcStdout: document.getElementById("tc-stdout"),
  tcStdoutTrailing: document.getElementById("tc-stdout-trailing"),
  addTestcase: document.getElementById("add-testcase"),
  clearTestcases: document.getElementById("clear-testcases"),
  buildTestsYaml: document.getElementById("build-tests-yaml"),
  testcasesList: document.getElementById("testcases-list"),
  solutionBody: document.getElementById("solution-body"),
  readmeBody: document.getElementById("readme-body"),
  stepButtons: Array.from(document.querySelectorAll(".step-btn")),
  stepPanes: Array.from(document.querySelectorAll(".step-pane")),
  prevStep: document.getElementById("prev-step"),
  nextStep: document.getElementById("next-step"),
  previewPath: document.getElementById("preview-path"),
  previewContent: document.getElementById("preview-content"),
  generatedTree: document.getElementById("generated-tree"),
  chooseFolder: document.getElementById("choose-folder"),
  writeFolder: document.getElementById("write-folder"),
  downloadTar: document.getElementById("download-tar"),
  fsHint: document.getElementById("fs-hint"),
  status: document.getElementById("status"),
};

const state = {
  activeStep: 0,
  outputDirHandle: null,
  testcases: [],
};

const year = new Date().getFullYear();
ui.copyright.value = `Copyright ${year} - Educatief gebruik met expliciete naamsvermelding`;

if (!ui.descriptionBody.value.trim()) {
  ui.descriptionBody.value = [
    "## Gevraagd",
    "Schrijf een programma of functie volgens de opgave.",
    "",
    "## Input",
    "Beschrijf welke invoer de leerling geeft.",
    "",
    "## Output",
    "Beschrijf exact welke uitvoer verwacht wordt.",
    "",
    "### Voorbeeld",
    "Voor invoer `2` verschijnt er:",
    "```",
    "Voorbeelduitvoer",
    "```",
  ].join("\n");
}

let seededDefaultTestcases = false;
if (!ui.testsBody.value.trim()) {
  ui.testsBody.value = [
    "- tab: Feedback",
    "  testcases:",
    "    - stdin: \"2\"",
    "      stdout: \"Voorbeelduitvoer\\n\"",
  ].join("\n");
  seededDefaultTestcases = true;
}

if (!ui.readmeBody.value.trim()) {
  ui.readmeBody.value = [
    "Deze oefening werd opgesteld voor educatief gebruik.",
    "",
    "Meer info: https://robbewulgaert.be",
  ].join("\n");
}

if (!ui.solutionBody.value.trim()) {
  ui.solutionBody.value = [
    "# Voorbeeldoplossing",
    "waarde = int(input())",
    "print(waarde)",
  ].join("\n");
}

if (seededDefaultTestcases) {
  state.testcases = [{ stdin: "2", stdout: "Voorbeelduitvoer\n" }];
}

function sanitizeFolderName(value, fallback) {
  const cleaned = String(value || "")
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9._-]+/g, "_")
    .replace(/^_+|_+$/g, "");
  return cleaned || fallback;
}

function normalizeMultiline(value) {
  const normalized = String(value || "").replace(/\r\n/g, "\n").trimEnd();
  return `${normalized}\n`;
}

function parseLabels(value) {
  return String(value || "")
    .split(",")
    .map((part) => part.trim())
    .filter(Boolean);
}

function escapeForYamlDoubleQuoted(value) {
  return String(value || "")
    .replace(/\\/g, "\\\\")
    .replace(/"/g, "\\\"")
    .replace(/\r/g, "")
    .replace(/\n/g, "\\n")
    .replace(/\t/g, "\\t");
}

function ensureTrailingNewline(value) {
  const normalized = String(value || "").replace(/\r\n/g, "\n");
  if (!normalized.endsWith("\n")) {
    return `${normalized}\n`;
  }
  return normalized;
}

function buildTestsYamlFromCases(cases) {
  const lines = [
    "- tab: Feedback",
    "  testcases:",
  ];

  cases.forEach((testcase) => {
    lines.push(`    - stdin: "${escapeForYamlDoubleQuoted(testcase.stdin)}"`);
    lines.push(`      stdout: "${escapeForYamlDoubleQuoted(testcase.stdout)}"`);
  });

  return lines.join("\n");
}

function renderTestcasesList() {
  ui.testcasesList.innerHTML = "";

  if (!state.testcases.length) {
    const empty = document.createElement("p");
    empty.className = "testcases-empty";
    empty.textContent = "Nog geen testcases toegevoegd.";
    ui.testcasesList.appendChild(empty);
    return;
  }

  state.testcases.forEach((testcase, index) => {
    const row = document.createElement("div");
    row.className = "testcase-item";

    const title = document.createElement("p");
    title.className = "testcase-title";
    title.textContent = `Testcase ${index + 1}`;

    const content = document.createElement("pre");
    content.className = "testcase-code";
    content.textContent = [
      `stdin: "${escapeForYamlDoubleQuoted(testcase.stdin)}"`,
      `stdout: "${escapeForYamlDoubleQuoted(testcase.stdout)}"`,
    ].join("\n");

    const removeButton = document.createElement("button");
    removeButton.type = "button";
    removeButton.className = "ghost-btn testcase-remove";
    removeButton.textContent = "Verwijder";
    removeButton.addEventListener("click", () => {
      state.testcases.splice(index, 1);
      renderTestcasesList();
      setStatus("Testcase verwijderd.", "warn");
    });

    row.appendChild(title);
    row.appendChild(content);
    row.appendChild(removeButton);
    ui.testcasesList.appendChild(row);
  });
}

function buildConfigObject(meta) {
  const config = {
    type: "exercise",
    programming_language: meta.language,
    evaluation: {
      handler: "TESTed",
      test_suite: meta.testSuite,
    },
    access: meta.access,
    description: {
      names: {
        nl: meta.titleNl,
        en: meta.titleEn,
      },
    },
    labels: parseLabels(meta.labels),
    copyright_notice: meta.copyright,
  };

  if (meta.contact) {
    config.contact = meta.contact;
  }

  return config;
}

function collectMeta() {
  const folder = sanitizeFolderName(ui.exerciseFolder.value, "nieuwe_oefening");
  const titleNl = ui.exerciseTitleNl.value.trim() || "Nieuwe oefening";
  const titleEn = ui.exerciseTitleEn.value.trim() || titleNl;
  const testSuite = sanitizeFolderName(ui.testSuite.value, "tests.yaml").replace(/\.yaml$/i, "") + ".yaml";

  return {
    folder,
    titleNl,
    titleEn,
    language: ui.language.value,
    access: ui.access.value,
    labels: ui.labels.value,
    contact: ui.contact.value.trim(),
    copyright: ui.copyright.value.trim() || `Copyright ${year}`,
    testSuite,
  };
}

function buildBundle() {
  const meta = collectMeta();
  const configObject = buildConfigObject(meta);
  const commentHash = `# ${meta.copyright}`;
  const commentHtml = `<!-- ${meta.copyright} -->`;

  const files = [
    {
      path: "config.json",
      content: `${JSON.stringify(configObject, null, 2)}\n`,
    },
    {
      path: "description/description.nl.md",
      content: `${commentHtml}\n\n${normalizeMultiline(ui.descriptionBody.value)}`,
    },
    {
      path: `evaluation/${meta.testSuite}`,
      content: `${commentHash}\n${normalizeMultiline(ui.testsBody.value)}`,
    },
    {
      path: "solution/solution.nl.py",
      content: `${commentHash}\n${normalizeMultiline(ui.solutionBody.value)}`,
    },
    {
      path: "readme.nl.md",
      content: `${commentHtml}\n\n${normalizeMultiline(ui.readmeBody.value)}`,
    },
  ];

  return { meta, files, configObject };
}

function insertPath(tree, path) {
  const parts = path.split("/");
  let node = tree;

  for (let i = 0; i < parts.length; i += 1) {
    const part = parts[i];
    const isFile = i === parts.length - 1;

    if (isFile) {
      node[part] = null;
    } else {
      if (!node[part] || node[part] === null) {
        node[part] = {};
      }
      node = node[part];
    }
  }
}

function formatTreeNode(node, prefix, lines) {
  const entries = Object.entries(node).sort((a, b) => {
    const aDir = a[1] !== null;
    const bDir = b[1] !== null;
    if (aDir !== bDir) {
      return aDir ? -1 : 1;
    }
    return a[0].localeCompare(b[0]);
  });

  entries.forEach(([name, child], index) => {
    const isLast = index === entries.length - 1;
    const connector = isLast ? "\\-- " : "|-- ";
    lines.push(`${prefix}${connector}${name}`);
    if (child) {
      const nextPrefix = `${prefix}${isLast ? "    " : "|   "}`;
      formatTreeNode(child, nextPrefix, lines);
    }
  });
}

function buildTreeText(bundle) {
  const root = {};
  bundle.files.forEach((file) => insertPath(root, file.path));

  const lines = ["gekozen_map/", `\\-- ${bundle.meta.folder}/`];
  formatTreeNode(root, "    ", lines);
  return lines.join("\n");
}

function getStepFileForPreview(bundle, stepIndex) {
  switch (stepIndex) {
    case 0:
      return bundle.files.find((file) => file.path === "config.json");
    case 1:
      return bundle.files.find((file) => file.path === "description/description.nl.md");
    case 2:
      return bundle.files.find((file) => file.path.startsWith("evaluation/"));
    case 3:
      return bundle.files.find((file) => file.path === "solution/solution.nl.py");
    case 4:
      return bundle.files.find((file) => file.path === "readme.nl.md");
    case 5:
    default:
      return bundle.files.find((file) => file.path === "config.json");
  }
}

function setStatus(message, tone = "ok") {
  ui.status.textContent = message;
  ui.status.className = `status ${tone}`;
}

function render() {
  const bundle = buildBundle();
  const stepFile = getStepFileForPreview(bundle, state.activeStep);

  ui.stepButtons.forEach((button, index) => {
    button.classList.toggle("active", index === state.activeStep);
  });

  ui.stepPanes.forEach((pane, index) => {
    pane.classList.toggle("active", index === state.activeStep);
  });

  ui.prevStep.disabled = state.activeStep === 0;
  ui.nextStep.disabled = state.activeStep === ui.stepPanes.length - 1;

  ui.configPreview.textContent = JSON.stringify(bundle.configObject, null, 2);
  ui.previewPath.textContent = stepFile.path;
  ui.previewContent.textContent = stepFile.content;
  ui.generatedTree.textContent = buildTreeText(bundle);
}

function switchStep(nextStep) {
  const bounded = Math.max(0, Math.min(ui.stepPanes.length - 1, nextStep));
  state.activeStep = bounded;
  render();
}

function getTarPathParts(path) {
  if (path.length <= 100) {
    return { name: path, prefix: "" };
  }

  const lastSlash = path.lastIndexOf("/");
  if (lastSlash <= 0) {
    throw new Error(`Pad is te lang voor TAR: ${path}`);
  }

  const prefix = path.slice(0, lastSlash);
  const name = path.slice(lastSlash + 1);

  if (name.length > 100 || prefix.length > 155) {
    throw new Error(`Pad is te lang voor TAR: ${path}`);
  }

  return { name, prefix };
}

function writeAscii(buffer, offset, value, length) {
  const text = String(value || "");
  for (let i = 0; i < length; i += 1) {
    buffer[offset + i] = i < text.length ? text.charCodeAt(i) : 0;
  }
}

function writeOctal(buffer, offset, value, length) {
  const octal = Number(value).toString(8);
  const padded = octal.padStart(length - 1, "0");
  writeAscii(buffer, offset, padded, length - 1);
  buffer[offset + length - 1] = 0;
}

function buildTarHeader(path, size) {
  const buffer = new Uint8Array(512);
  const { name, prefix } = getTarPathParts(path);

  writeAscii(buffer, 0, name, 100);
  writeOctal(buffer, 100, 0o644, 8);
  writeOctal(buffer, 108, 0, 8);
  writeOctal(buffer, 116, 0, 8);
  writeOctal(buffer, 124, size, 12);
  writeOctal(buffer, 136, Math.floor(Date.now() / 1000), 12);
  writeAscii(buffer, 148, "        ", 8);
  writeAscii(buffer, 156, "0", 1);
  writeAscii(buffer, 257, "ustar", 5);
  buffer[262] = 0;
  writeAscii(buffer, 263, "00", 2);
  writeAscii(buffer, 345, prefix, 155);

  let checksum = 0;
  for (let i = 0; i < 512; i += 1) {
    checksum += buffer[i];
  }

  const checksumText = checksum.toString(8).padStart(6, "0");
  writeAscii(buffer, 148, checksumText, 6);
  buffer[154] = 0;
  buffer[155] = 32;

  return buffer;
}

function createTarBlob(bundle) {
  const encoder = new TextEncoder();
  const blocks = [];

  bundle.files.forEach((file) => {
    const path = `${bundle.meta.folder}/${file.path}`;
    const data = encoder.encode(file.content);
    const header = buildTarHeader(path, data.length);
    blocks.push(header);
    blocks.push(data);

    const paddingLength = (512 - (data.length % 512)) % 512;
    if (paddingLength > 0) {
      blocks.push(new Uint8Array(paddingLength));
    }
  });

  blocks.push(new Uint8Array(1024));
  return new Blob(blocks, { type: "application/x-tar" });
}

async function writeBundleToDirectory(bundle) {
  if (!state.outputDirHandle) {
    throw new Error("Kies eerst een lokale map.");
  }

  const exerciseHandle = await state.outputDirHandle.getDirectoryHandle(bundle.meta.folder, { create: true });

  for (const file of bundle.files) {
    const parts = file.path.split("/");
    const fileName = parts.pop();
    let targetDir = exerciseHandle;

    for (const part of parts) {
      targetDir = await targetDir.getDirectoryHandle(part, { create: true });
    }

    const fileHandle = await targetDir.getFileHandle(fileName, { create: true });
    const writable = await fileHandle.createWritable();
    await writable.write(file.content);
    await writable.close();
  }
}

function setupEvents() {
  ui.stepButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const next = Number.parseInt(button.dataset.step || "0", 10);
      switchStep(next);
    });
  });

  ui.prevStep.addEventListener("click", () => switchStep(state.activeStep - 1));
  ui.nextStep.addEventListener("click", () => switchStep(state.activeStep + 1));

  const liveInputs = [
    ui.exerciseFolder,
    ui.exerciseTitleNl,
    ui.exerciseTitleEn,
    ui.language,
    ui.access,
    ui.labels,
    ui.contact,
    ui.copyright,
    ui.testSuite,
    ui.descriptionBody,
    ui.testsBody,
    ui.solutionBody,
    ui.readmeBody,
  ];

  liveInputs.forEach((input) => {
    input.addEventListener("input", render);
    input.addEventListener("change", render);
  });

  ui.addTestcase.addEventListener("click", () => {
    const stdin = String(ui.tcStdin.value || "").replace(/\r\n/g, "\n");
    const rawStdout = String(ui.tcStdout.value || "").replace(/\r\n/g, "\n");
    const stdout = (ui.tcStdoutTrailing.checked && rawStdout.length > 0)
      ? ensureTrailingNewline(rawStdout)
      : rawStdout;

    if (!stdin.trim() && !stdout.trim()) {
      setStatus("Vul minstens stdin of stdout in voor je een testcase toevoegt.", "warn");
      return;
    }

    state.testcases.push({ stdin, stdout });
    renderTestcasesList();

    ui.tcStdin.value = "";
    ui.tcStdout.value = "";
    setStatus("Testcase toegevoegd. Klik op 'Genereer tests.yaml' om de YAML te verversen.", "ok");
  });

  ui.clearTestcases.addEventListener("click", () => {
    state.testcases = [];
    renderTestcasesList();
    setStatus("Alle testcases gewist.", "warn");
  });

  ui.buildTestsYaml.addEventListener("click", () => {
    if (!state.testcases.length) {
      setStatus("Er zijn nog geen testcases om tests.yaml te genereren.", "warn");
      return;
    }

    ui.testsBody.value = buildTestsYamlFromCases(state.testcases);
    render();
    setStatus("tests.yaml gegenereerd op basis van de testcase-assistent.", "ok");
  });

  ui.chooseFolder.addEventListener("click", async () => {
    if (typeof window.showDirectoryPicker !== "function") {
      setStatus("Deze browser ondersteunt geen mapselectie. Gebruik Download .tar.", "warn");
      return;
    }

    try {
      state.outputDirHandle = await window.showDirectoryPicker({ mode: "readwrite" });
      setStatus("Lokale map gekozen. Je kan nu de bestanden rechtstreeks wegschrijven.", "ok");
    } catch (error) {
      if (error && error.name === "AbortError") {
        setStatus("Mapselectie geannuleerd.", "warn");
      } else {
        setStatus(`Mapselectie mislukt: ${error.message}`, "err");
      }
    }
  });

  ui.writeFolder.addEventListener("click", async () => {
    const bundle = buildBundle();

    try {
      await writeBundleToDirectory(bundle);
      setStatus(`Bestanden geschreven naar de gekozen map in ${bundle.meta.folder}/.`, "ok");
    } catch (error) {
      setStatus(`Schrijven mislukt: ${error.message}`, "err");
    }
  });

  ui.downloadTar.addEventListener("click", () => {
    try {
      const bundle = buildBundle();
      const blob = createTarBlob(bundle);
      const filename = `${bundle.meta.folder}.tar`;
      const url = URL.createObjectURL(blob);
      const anchor = document.createElement("a");
      anchor.href = url;
      anchor.download = filename;
      document.body.appendChild(anchor);
      anchor.click();
      anchor.remove();
      URL.revokeObjectURL(url);
      setStatus(`TAR gedownload als ${filename}.`, "ok");
    } catch (error) {
      setStatus(`Download mislukt: ${error.message}`, "err");
    }
  });
}

function init() {
  if (typeof window.showDirectoryPicker === "function") {
    ui.fsHint.textContent = "Tip: kies de map waar je index.html staat om de output in dezelfde root te schrijven.";
  } else {
    ui.fsHint.textContent = "Je browser ondersteunt geen directe mappen-write. Gebruik de .tar download als fallback.";
  }

  setupEvents();
  renderTestcasesList();
  render();
}

init();
