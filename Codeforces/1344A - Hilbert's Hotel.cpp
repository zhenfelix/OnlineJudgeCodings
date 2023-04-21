#include<bits/stdc++.h>
using namespace std;

int main() {
    // freopen("contests/input","r",stdin);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        bool flag = true;
        vector<int> cnt(n,0);
        for (int i = 0; i < n; i++) {
            int a;
            cin >> a;
            a = (a+i)%n;
            a = (a+n)%n;
            cnt[a]++;
            if (cnt[a] > 1) flag = false;
        }
        if (flag) cout << "YES\n";
        else cout << "NO\n";
    }
    return 0;
}

// int main() {
//     cout << (-8)%7;
//     return 0;
// }