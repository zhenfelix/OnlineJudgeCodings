// #include <bits/stdc++.h>
#include <vector>
#include <algorithm>
#include <climits>
#include <iostream>
#include <unordered_map>

using namespace std;
using ll = long long;
using pii = pair<int,int>;

const int inf = 0x3f3f3f3f;
int t, n, k;



void solve(){
    cin >> n >> k;
    vector<int> bn(n);
    unordered_map<int,int> mp;
    mp[0] = 0;
    int res = inf;
    for (int i = 0; i < n; i++)
        cin >> bn[i];
    for (int i = 0; i < n; i++){
        int sums = 0;
        for (int j = i-1; j>= 0 && sums <= k; j--){
            sums += bn[j];
            if (mp.count(sums)){
                mp[sums] = min(mp[sums], i-j);
            }
            else{
                mp[sums] = i-j;
            }
        }
        sums = 0;
        for (int j = i; j < n && sums <= k; j++){
            sums += bn[j];
            if (mp.count(k-sums)){
                res = min(res, mp[k-sums]+j-i+1);
            }
        }
    }
    if (res == inf)
        cout << -1 << endl;
    else
        cout << res << endl;
    return;
}

int main()
{
    // freopen("input", "r", stdin);
    cin >> t;
    
    for (int i = 1; i <= t; i++){
        cout << "Case #" << i << ": ";
        solve();
    }
}
