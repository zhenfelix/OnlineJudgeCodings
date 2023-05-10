
#include <bits/stdc++.h>
using namespace std;

#define NO cout<<"NO\n";return 0;

int main() {
    // freopen("contests/input","r",stdin);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n,k;
    cin >> n >> k;
    if (n < k) {
        // cout << "NO\n";
        // return 0;
        NO
    }
    vector<int> bits(30,0);
    int cnt = 0;
    for (int i = 0; i < 30 && n; i++) {
        if (n&1) {
            bits[i]++;
            cnt++;
        }
        n >>= 1;
    }
    if (k < cnt) {
        NO
    }
    k -= cnt;
    for (int i = 29; i > 0 && k; i--) {
        while (bits[i] && k) {
            bits[i]--;
            bits[i-1] += 2;
            k--;
        }
    }
    cout << "YES\n";
    for (int i = 0, b = 1; i < 30; i++) {
        while (bits[i]) {
            cout << b << " ";
            bits[i]--;
        }
        b <<= 1;
    }
    return 0;
}