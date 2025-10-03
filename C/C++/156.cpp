#include <iostream>
#include <string>
using namespace std;

int main(){
    int N;
    cin >> N;
    string l1, l2;
    int ans = 0;

    for (int i = 0; i < N; i++){
        cin >> l1 >> l2;

        // stoi(list名.substr(start,数))でlistのどこからどこまでを持ってくるかを指定
        int hh1 = stoi(l1.substr(0, 2));
        int mm1 = stoi(l1.substr(3, 2));
        int hh2 = stoi(l2.substr(0, 2));
        int mm2 = stoi(l2.substr(3, 2));

        ans += (hh2 * 60 + mm2) - (hh1 * 60 + mm1);
    }

    cout << ans / 60 << " " << ans % 60 << endl;
    return 0;

}