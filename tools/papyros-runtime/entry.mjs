// Export one graph so Papyros and Delphi share the same backend registry and
// Comlink callback markers. Do not bundle these entry points independently.
export { papyros } from "@dodona/papyros/dist/frontend/state/Papyros.js";
export { BackendManager } from "@dodona/papyros/dist/communication/BackendManager.js";
export { makeChannel } from "sync-message";
export { proxy as ComlinkProxy } from "comlink";
