#include <bits/stdc++.h>
constexpr int P = 1000000007;
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    
    int n, x, pos;
    std::cin >> n >> x >> pos;
    int l = 0, r = n;
    int L = 0, R = 0;
    while (l < r) {
        int m = (l + r) / 2;
        if (pos < m) r = m, ++R;
        else l = m + 1, L += m != pos;
    }
    int ans = 1;
    for (int i = 1; i <= L; ++i) ans = int64_t(ans) * (x - i) % P;
    for (int i = 1; i <= R; ++i) ans = int64_t(ans) * (n - x - i + 1) % P;
    for (int i = 1; i <= n - L - R - 1; ++i) ans = int64_t(ans) * i % P;
    std::cout << ans << "\n";
    
    return 0;
}



#include<bits/stdc++.h>
using namespace std;
using ll = long long;

const int MOD = 1e9+7;

ll quickmul(ll a, int q) {
    ll res = 1;
    while (q)
    {
        if (q&1) res = (res*a)%MOD;
        q >>= 1;
        a = (a*a)%MOD;
    }
    return res;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    // freopen("contests/input","r",stdin);
    int n, x, pos;
    cin >> n >> x >> pos;
    int l = 0, r = n, big = 0, small = 0;
    while (l < r){
        int m = (l+r)/2;
        if (m > pos) {
            big++;
            r = m;
        }
        else {
            if (m < pos) small++;
            l = m+1;
        }
    }
    if (n-x < big || x-1 < small) {
        cout << 0 << endl;
        return 0;
    }
    
    vector<ll> fs(n+1,1), invfs(n+1,1);
    for (int i = 1; i <= n; i++) fs[i] = (fs[i-1]*i)%MOD;
    invfs[n] = quickmul(fs[n],MOD-2);
    for (int i = n; i >= 1; i--) invfs[i-1] = (invfs[i]*i)%MOD;
    ll res = 1;
    res = (((res*fs[n-x])%MOD)*invfs[n-x-big])%MOD;
    res = (((res*fs[x-1])%MOD)*invfs[x-1-small])%MOD;
    res = (res*fs[n-1-big-small])%MOD;
    cout << res << endl;
    return 0;
}
