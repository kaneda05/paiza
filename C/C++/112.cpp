#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int N;
    cin >> N;

    int minTime = 1e9;
    int maxTime = -1e9;

    for (int i = 0; i < N; i++){
        int s, t, f;
        cin >> s >> f >> t;
        int dayLength = s + f + (24 - t);

        minTime = min(minTime, dayLength);
        maxTime = max(maxTime, dayLength);
    }

    cout << minTime << endl;
    cout << maxTime << endl;
    return 0;
}