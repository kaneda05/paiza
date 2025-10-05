#include <bits/stdc++.h>
using namespace std;

int main(){
    int M;
    cin >> M;
    vector<int> A(M);
    for (int i = 0; i < M; i++) cin >> A[i];

    int N;
    cin >> N;
    vector<int> B(N);
    for (int i = 0; i < N; i++) cin >> B[i];

    vector<string> date(32, "x");
    bool flag = true;

    for (int i = 1; i < 32; i++){
        bool inA = find(A.begin(), A.end(), i) != A.end();
        bool inB = find(B.begin(), B.end(), i) != B.end();

        if (inA && inB){
            if (flag){
                date[i] = "A";
                flag = false;
            }else{
                date[i] = "B";
                flag = true;
            }
        }else if (inA){
            date[i] = "A";
        }else if (inB){
            date[i] = "B";
        }
    }
    for (int i = 1; i < 32; i++){
        cout << date[i] << endl;
    }

    return 0;
}