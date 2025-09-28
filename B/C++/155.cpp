#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int H, W, N;
    cin >> H >> W >> N;

    vector<vector<string>> stamps(N, vector<string>(H));
    for (int k = 0; k < N; k++){
        for (int i = 0; i < H; i++){
            cin >> stamps[k][i];
        }
    }

    int R, C;
    cin >> R >> C;
    vector<vector<int>> B(R, vector<int>(C));
    for (int i = 0; i < R; i++){
        for (int j = 0; j < C; j++){
            cin >> B[i][j];
            B[i][j]--;
        }
    }

    for (int i = 0; i < R; i++){
        for (int subrow = 0; subrow < H; subrow++){
            for (int j = 0; j < C; j++){
                cout << stamps[B[i][j]][subrow];
            }

            cout << "\n";
        }
    }

    return 0;
}