const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

const n = input[0];
const m = input[1];

console.log(n - m);