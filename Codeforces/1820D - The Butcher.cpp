
#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <queue>
#include <set>
using namespace std;
using ll = long long;
void solve(int n, vector<vector<int>> arr) {
    // MOD = 998244353
    vector<tuple<int,int,int>> qh, qw;
    for (int i = 0; i < n; i++) {
        int h = arr[i][0];
        int w = arr[i][1];
        qh.push_back(make_tuple(h,0,i));
        qw.push_back(make_tuple(w,1,i));
    }
    auto check = [&](vector<tuple<int,int,int>> q1,vector<tuple<int,int,int>> q2) {
        set<int> visited;
        vector<pair<int,int>> seq;
        make_heap(q1.begin(),q1.end());
        make_heap(q2.begin(),q2.end());
        while (!q1.empty() || !q2.empty()) {
            while (!q1.empty() && visited.count(get<2>(q1.front()))) {
                pop_heap(q1.begin(),q1.end());
                q1.pop_back();
            }
            if (q1.empty()) break;
            int cur = get<0>(q1.front());
            while (!q1.empty()) {
                if (get<0>(q1.front()) != cur) break;
                int k = get<1>(q1.front());
                int i = get<2>(q1.front());
                pop_heap(q1.begin(),q1.end());
                q1.pop_back();
                if (!visited.count(i)) {
                    visited.insert(i);
                    seq.push_back(make_pair(i,k));
                }
            }
            while (!q2.empty() && visited.count(get<2>(q2.front()))) {
                pop_heap(q2.begin(),q2.end());
                q2.pop_back();
            }
            if (q2.empty()) break;
            cur = get<0>(q2.front());
            while (!q2.empty()) {
                if (get<0>(q2.front()) != cur) break;
                int k = get<1>(q2.front());
                int i = get<2>(q2.front());
                pop_heap(q2.begin(),q2.end());
                q2.pop_back();
                if (!visited.count(i)) {
                    visited.insert(i);
                    seq.push_back(make_pair(i,k));
                }
            }
        }
        if (seq.size() < n) return vector<ll>();
        reverse(seq.begin(),seq.end());
        vector<ll> ans(2);
        int si = seq[0].first;
        int sk = seq[0].second;
        ans[sk] = arr[si][sk];
        for (auto p : seq) {
            int i = p.first;
            int k = p.second;
            if (arr[i][k] == ans[k]) {
                ans[1-k] += arr[i][1-k];
            } else if (arr[i][1-k] == ans[1-k]) {
                ans[k] += arr[i][k];
            } else {
                return vector<ll>();
            }
        }
        return ans;
    };
    
    set<pair<ll,ll>> res;
    make_heap(qh.begin(),qh.end());
    make_heap(qw.begin(),qw.end());
    vector<ll> tmp = check(qh,qw);
    if (!tmp.empty()) res.insert(make_pair(tmp[0],tmp[1]));
    tmp = check(qw,qh);
    if (!tmp.empty()) res.insert(make_pair(tmp[0],tmp[1]));
    cout << res.size() << endl;
    for (auto p : res) {
        cout << p.first << " " << p.second << endl;
    }
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("contests/input", "r", stdin);
#endif
    int t;
    cin >> t;
    // t = 1
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        vector<vector<int>> arr(n,vector<int>(2));
        for (int j = 0; j < n; j++) cin >> arr[j][0] >> arr[j][1];
        solve(n,arr);
    }
    return 0;
}