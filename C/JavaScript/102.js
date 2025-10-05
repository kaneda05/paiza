const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n").map(Number);

let = idx = 0;
const M = input[idx++];
const A = input.slice(idx, idx + M);

idx += M;

const N = input[idx++];
const B = input.slice(idx, idx + N);

let date = Array(32).fill("x");
let flag = true;

for (let i = 1; i < 32; i++){
    let inA = A.includes(i);
    let inB = B.includes(i);

    if (inA && inB){
        if (flag){
            date[i] = "A";
            flag = false
        }else{
            date[i] = "B";
            flag = true;
        }
    }else if(inA){
        date[i] = "A";
    }else if(inB){
        date[i] = "B";
    }
}

for (let i = 1; i < 32; i++){
    console.log(date[i]);
}