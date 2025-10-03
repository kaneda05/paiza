const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const N = parseInt(input[0], 10);
let minTime = Infinity;
let maxTime = -Infinity;

for (let i = 1; i <= N; i++){
    const [s, f, t] = input[i].split(" ").map(Number);
    const dayLength = s + f + (24 - t);
    minTime = Math.min(minTime, dayLength);
    maxTime = Math.max(maxTime, dayLength);
}

console.log(minTime);
console.log(maxTime);