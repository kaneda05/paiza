const fs = require("fs");
const name = fs.readFileSync(0, "utf8").trim();
const vowels = "aiueoAIUEO";
let ans = "";

for (let i = 0; i < name.length; i++){
    if (!vowels.includes(name[i])){
        ans += name[i];
    }
}

console.log(ans);