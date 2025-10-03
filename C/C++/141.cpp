#include <iostream>
#include <vector>
#include <map>
#include <string>
using namespace std;

int main(){
    int N;
    cin >> N;
    vector<string> A(N);
    for (int i = 0; i < N; i++){
        cin >> A[i];
    }

    // PythonのCounterの役割
    // mapで辞書の作成
    // 辞書の形式を<string, int> 辞書名
    map<string, int> c;
    for (auto &s : A){
        c[s]++;
    }

    int ans = -1;
    string name = "";
    // map<first,second> → <名前, 投票数>
    for (auto &p : c){
        if (ans < p.second){
            ans = p.second;
            name = p.first;
        }
    }

    cout << name << endl;
    return 0;
}