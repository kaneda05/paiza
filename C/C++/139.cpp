#include <iostream>
#include <set>
using namespace std;

int main(){
    int N;
    cin >> N;
    set<int> x_set;

    for (int i=0; i<N; i++){
        int x;
        cin >> x;
        if (x <= N){
            x_set.insert(x);
        }
    }

    cout << N - x_set.size() << endl;
    return 0;
}