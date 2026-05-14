let domain = "example.com";
let escaped = domain.replace(/\./g, "\\.");

let regex = new RegExp(`\\b(?:[a-zA-Z0-9-]+\\.)+${escaped}\\b`, "g");

let results = [...new Set(
  [...document.body.innerText.matchAll(regex)].map(m => m[0])
)];

console.log(results);