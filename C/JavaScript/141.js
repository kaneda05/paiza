const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const N = parseInt(input[0], 10);
const A = input.slice(1, N + 1);

// const xx = {}で辞書型を作るのはPythonに類似
const c = {};
for (let s of A){
    c[s] = (c[s] || 0) + 1; // sがまだ出ていない場合は0にして、すでにある場合は追加(Javaに似ている方法)
}

// constと違い格納した値が変わる可能性があるのでlet
let ans = -1;
let name = "";
for (let key in c){
    if (ans < c[key]){
        ans = c[key]
        name = key;
    }
}

console.log(name);