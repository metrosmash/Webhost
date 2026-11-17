// Both local and deployed API bases include the /api prefix.

// js/config.js
const isLocal = ["127.0.0.1", "localhost","[::1]"].includes(window.location.hostname);

export const API_BASE = isLocal ? "http://127.0.0.1:8000/api" : "/api";