#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){
    int N;
    cin >> N;
    vector<string> ls(N);
    for (int i = 0; i < N; i++){
        cin >> ls[i];
    }

    for (int i = 0; i < N - 1; i++){
        char lastChar = ls[i].back();
        char firstChar = ls[i+1][0];

        if (lastChar == firstChar){
            continue;
        }else{
            cout << lastChar << " " << firstChar << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;
    return 0;
}