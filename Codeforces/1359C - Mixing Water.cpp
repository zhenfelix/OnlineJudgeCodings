
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

int t, n, q;
// int a[maxn];
// ll s[maxn], mx;

void solve()
{
    ll h,c,t, ans, k;
    double m;
    scanf("%lld%lld%lld\n", &h, &c, &t);
    if (t*2 <= (h+c)){
        ans = 2;
    }
    else if (h == t){
        ans = 1;
    }
    else{
        k = (h-t-1)/(2*t-h-c) + 1;
        if ((double)(k*h+(k-1)*c)/(2*k-1) - t <= t - (double)((k+1)*h+k*c)/(2*k+1)){
            ans = 2*k-1;
        }
        else{
            ans = 2*k+1;
        }
    }
    printf("%d\n", ans);
}

int main()
{
    // freopen("input", "r", stdin);
    scanf("%d\n", &t);
    for(int i = 0; i < t; i++){
        solve();
    }
}
