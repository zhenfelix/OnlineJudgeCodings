
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
    ll a,b,x,y,cnt=0;
    scanf("%lld%lld\n", &a, &b);
    cnt += a+b;
    x = (a<<1) + b;
    scanf("%lld%lld\n", &a, &b);
    cnt += a + b;
    y = (a << 1) + b;
    if (cnt == 0)
        printf("%d\n", 0);
    else if (cnt < 4){
        printf("%d\n", 1);
    }
    else{
        printf("%d\n", 2);
    }
    
}

int main()
{
    // freopen("input", "r", stdin);
    scanf("%d\n", &t);
    for(int i = 0; i < t; i++){
        solve();
    }
}
