
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
ll MOD = 998244353;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
#ifndef ONLINE_JUDGE 
    freopen("input","r",stdin);
#endif
    int n,k;
    cin >> n >> k;
    vector<int> arr(n);
    ll ans = 0, s = 0;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        s += arr[i];
    }
    ll mask = 1;
    while (s) {
        s >>= 1;
        mask <<= 1;
    }
    mask >>= 1;
    while (mask) {
        int cnt = 0;
        for (int i = 0; i < n && cnt < k; i++) {
            s = 0;
            for (int j = i; j < n && cnt < k; j++) {
                s += arr[j];
                if (((s&ans) == ans) && (s&mask)) ++cnt;
            }
        }
        if (cnt >= k) ans |= mask;
        mask >>= 1;
    }
    cout << ans << endl;
    return 0;
}