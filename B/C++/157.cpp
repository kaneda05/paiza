#include <iostream>
#include <vector>
#include <set>
#include <climits>
using namespace std;

int main(){
    int N, K;
    cin >> N >> K;
    vector<vector<int>> p(N, vector<int>(K));

    for (int i = 0; i < N; i++){
        for (int j = 0; j < K; j++){
            cin >> p[i][j];
        }
    }
    set<int> shop_number;
    for (int k = 0; k < K; k++){
        int min_pnk = 100000;
        int min_shop = -1;
        for (int n = 0; n < N; n++){
            if (p[n][k] < min_pnk){
                min_pnk = p[n][k];
                min_shop = n;
            }
        }
    shop_number.insert(min_shop);
    }
    
    cout << shop_number.size() << endl;
    return 0;
}
