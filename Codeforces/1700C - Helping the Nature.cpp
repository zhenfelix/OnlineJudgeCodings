
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

int arr[maxn];

void solve()
{
    int n;
    ll ans = 0, right = 0;
    scanf("%d\n", &n);
    for (int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
        if (i > 0){
            ll tmp = arr[i]-arr[i-1];
            if (tmp > 0){
                ans += tmp;
                right += tmp;
            }
            else{
                ans -= tmp;
            }
        }
    }
    ll tmp = arr[n-1]-right;
    ans += tmp > 0 ? tmp : -tmp;
    printf("%lld\n", ans); 
}

int main()
{
    // freopen("input", "r", stdin);
    int t;
    scanf("%d\n", &t);
    for(int i = 0; i < t; i++){
        solve();
    }
}
