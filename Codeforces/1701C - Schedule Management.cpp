
// #include <bits/stdc++.h>
#include <vector>
#include <algorithm>
#include <climits>
#include <iostream>
#include <unordered_map>
#include <cstring>

using namespace std;
using ll = long long;
using pii = pair<int, int>;

const int inf = 0x3f3f3f3f;
const int maxn = 200005;

int t, n, m, tmp;
int a[maxn], b[maxn];
// ll s[maxn], mx;

void solve()
{
    scanf("%d%d\n", &n, &m);
    memset(a, 0, (n+1)*sizeof(int));
    for (int i = 1; i <= m; i++){
        scanf("%d", &tmp);
        a[tmp] += 1;
    }
    ll lo = 1, hi = m*2;
    while (lo <= hi){
        ll mid = (lo+hi)/2;
        ll cnt = 0;
        for (int i = 1; i <= n; i++){
            cnt += min((int) mid,a[i]);
            if (mid > a[i]) cnt += (mid-a[i])/2;
        }
        if (cnt >= m){
            hi = mid - 1;
        }
        else{
            lo = mid + 1;
        }
    }
    printf("%lld\n", lo);
    
}

int main()
{
    // freopen("input", "r", stdin);
    scanf("%d\n", &t);
    for(int i = 0; i < t; i++){
        solve();
    }
}
