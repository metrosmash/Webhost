// js frontend api 
import { API_BASE } from "./config.js";


export async function greet(name) {
  const res = await fetch(`${API_BASE}/name?name=${encodeURIComponent(name)}`);
  if (!res.ok) {
    throw new Error(`Request failed: ${res.status}`);
  }
  return res.json();
}