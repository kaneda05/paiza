#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, M;
    cin >> N >> M;
    vector<vector<int>> winners(N+1);

    for (int i = 0; i < M; i++){
        int x, y;
        cin >> x >> y;
        winners[x].push_back(y);

        if (!winners[y].empty()){
            for (int j : winners[y]){
                winners[x].push_back(j)
            }
        }
        winners[y].clear()
    }
    vector<int> counts(N+1,0);
    for (int i = 1; i < N; i++){
        counts[i] = winners[i].size();
    }

    int max_winner = *max_element(counts.begin() + 1, counts.end());

    for (int i = 1; i < N; i++){
        if(counts[i] == max_winner){
            cout << i << "\n";
        }
    }
    return 0;
}