const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const N = parseInt(input[0], 10);

for (let i = 0; i < N; i++){
    let s = input[1 + i*2].split("");
    let t = input[2 + i*2].split("");

    s.sort()
    t.sort();

    if (s.join("")==t.join("")){
        console.log("Yes");
    }else{
        console.log("No");
    }
}