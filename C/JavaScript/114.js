const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const N = parseInt(input[0], 10);
const ls = input.slice(1, N+1);

for (let i = 0; i<N-1; i++){
    const lastChar = ls[i][ls[i].length - 1];
    const firstChar = ls[i+1][0];

    if (lastChar == firstChar){
        continue;
    }else{
        console.log(lastChar, firstChar);
        process.exit(0);
    }
}

console.log("Yes")