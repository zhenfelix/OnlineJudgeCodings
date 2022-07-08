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


void solve()
{
    ll n, m, ans;
    scanf("%lld%lld\n", &n, &m);
    // vector<vector<int>> mat(n, vector<int>(n));
    ans = n*(n-1)*m/2+m*(m+1)/2+m*(n-1);
    printf("%lld\n",ans); 
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