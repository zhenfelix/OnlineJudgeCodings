

#include <bits/stdc++.h>
using namespace std;

int main() {
    // freopen("contests/input","r",stdin);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    string s, t;
    for (int i = 0; i < n; i++) {
        cin >> s >> t;
        string a, b;
        vector<int> cnt(3,0);
        for (auto ch : s) {
            if (ch == 'm') cnt[0]++;
            else if (ch == 'h') cnt[1]++;
            else if (ch == 'y') cnt[2]++;
            else a.push_back(ch);
        }
        for (auto ch : t) {
            if (ch == 'm') cnt[0]--;
            else if (ch == 'h') cnt[1]--;
            else if (ch == 'y') cnt[2]--;
            else b.push_back(ch);
        }
        bool flag = ((cnt[0] == cnt[1]) & (cnt[0] == cnt[2]));
        // for (int i = 0; i < 3; i++) if (cnt[i]%3) flag = false;
        if (a != b || !flag) cout << "No\n";
        else cout << "Yes\n";
    }
    return 0;
}