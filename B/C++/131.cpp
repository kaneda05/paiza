#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<vector<int>> A(N, vector<int>(M));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> A[i][j];
        }
    }

    int X;
    cin >> X;
    vector<pair<int, int>> route(X);
    for (int i = 0; i < X; i++) {
        cin >> route[i].first >> route[i].second;
    }

    int cur_line = 1, cur_station = 1;
    int total_cost = 0;

    for (auto [Ri, Si] : route) {
        Ri--;  // 0-index化
        Si--;
        total_cost += abs(A[Ri][Si] - A[Ri][cur_station - 1]);
        cur_line = Ri + 1;
        cur_station = Si + 1;
    }

    cout << total_cost << endl;
    return 0;
}
