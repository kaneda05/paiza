const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);
let winners = Array.from({ length: N+1}, () => []);

for (let i = 0; i < M; i++){
    let [x, y] = input[i+1].split(" ").map(Number);

    winners[x].push(y);
    if (winners[y].length > 0){
        winners[x].push(...winners[y]);
    }
    winners[y] = [];
}

let counts = Array(N+1).fill(0);
for (let i = 1; i <= N; i++){
    counts[i] = winners[i].length;
}

let maxwinner = Math.max(...counts.slice(1));

for (let i = 1; i <= N; i++){
    if (counts[i] === maxwinner){
        console.log(i);
    }
}