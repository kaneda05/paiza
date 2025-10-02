#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(){
    int N;
    cin >> N;
    for (int i = 0; i < N; i++){
        string s, t;
        cin >> s >> t;

        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        if (s == t){
            cout << "Yes" << endl;
        }else{
            cout << "No" << endl;
        }
    }
    return 0;
}