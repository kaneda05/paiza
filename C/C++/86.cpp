#include <bits/stdc++.h>
using namespace std;

int main(){
    string name;
    cin >> name;
    string vowels = "aiueoAIUEO";
    string ans = "";

    for (char c : name){
        if (vowels.find(c) == string::npos){
            ans += c
        }
    }
    cout << ans << endl;
    return 0;
}