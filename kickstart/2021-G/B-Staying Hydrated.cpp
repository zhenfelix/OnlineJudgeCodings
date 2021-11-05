// #include <bits/stdc++.h>
#include <vector>
#include <algorithm>
#include <climits>
#include <iostream>

using namespace std;
using ll = long long;
using pii = pair<int,int>;

int x1, x2, y1, y2, t, n;

void helper(vector<int> lo, vector<int> hi){
    sort(lo.begin(), lo.end());
    sort(hi.begin(), hi.end());
    vector<ll> slo = {0}, shi = {0};
    for (int i = 0; i < n; i++){
        slo.push_back(slo.back()+lo[i]);
        shi.push_back(shi.back()+hi[i]);
    }
    ll sums = LONG_MAX;
    int idx = -1, i = 0, j = 0, k;
    for (; i < n || j < n;){
        if (j == n || (i < n && lo[i] < hi[j])){
            k = lo[i++];
        }
        else{
            k = hi[j++];
        }
        ll left = j, right = n-i;
        ll csums = k*left-shi[left]+slo[n]-slo[i]-k*right;
        // cout << i << " " << j << endl;
        // cout << k << " " << left << " " << right << " " << csums << endl;
        if (csums < sums){
            sums = csums;
            idx = k;
        }
    }
    cout << idx;
    return;
}

void solve(){
    cin >> n;
    vector<int> xlo, xhi, ylo, yhi;
    for (int i = 0; i < n; i++){
        cin >> x1 >> y1 >> x2 >> y2;
        xlo.push_back(x1);
        xhi.push_back(x2);
        ylo.push_back(y1);
        yhi.push_back(y2);     
    }
    helper(xlo,xhi);
    cout << " ";
    helper(ylo,yhi);
    cout << endl;
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
