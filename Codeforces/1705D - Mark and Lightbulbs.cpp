// #include <bits/stdc++.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <climits>
#include <iostream>
#include <unordered_map>
#include <cstring>
#include <queue>

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using pci = pair<char, int>;

const int inf = 0x3f3f3f3f;
const int maxn = 200005;
const int maxch = 26;
const int maxm = 100;

int t, n, m, x, y, c, q;
// int a[maxn], b[maxn], idx[maxn], lo[maxn], hi[maxn];
// ll u[maxn];
ll l[maxm],r[maxm],lo[maxm],hi[maxm];
char arr[maxn], target[maxn];
ll k, sz;
string s;
ll cnt[maxch];
// ll s[maxn], mx;

std::ostream &operator<<(std::ostream &stream,
                         vector<pii> &v)
{
    for (auto [ch,i] : v) stream << ch << ": " << i << " ";
    return stream;
}

vector<pii> transform(char a[]){
    int lo = n, hi = -1;
    a[n] = '0';
    vector<pii> v;
    for (int i = 0; i <= n; i++){
        if (a[i] == '1'){
            lo = min(lo, i);
            hi = max(hi, i);
        }
        else{
            if (lo != n) v.push_back({lo,hi});
            lo = n;
        }
    }
    return v;
}

ll solve()
{
    scanf("%d\n", &n);
    scanf("%s\n", arr);
    scanf("%s\n", target);
    if (arr[0]!=target[0] || arr[n-1]!=target[n-1]) return -1;
    vector<pii> va, vb;
    va = transform(arr);
    vb = transform(target);
    // cout << va << endl;
    // cout << vb << endl;
    if (va.size() != vb.size()) return -1;
    m = va.size();
    ll ans = 0;
    for (int i = 0; i < m; i++){
        auto [la, ra] = va[i];
        auto [lb, rb] = vb[i];
        ans += (ll)abs(la-lb) + (ll)abs(ra-rb);

    }
    return ans;
}

int main()
{
    // freopen("input", "r", stdin);
    scanf("%d\n", &t);
    // for(int i = 0; i < t; i++){
    //     if (solve()){
    //         printf("YES\n");
    //     }
    //     else{
    //         printf("NO\n");
    //     }
    // }
    for (int i = 0; i < t; i++)
    {
        ll res = solve();
        printf("%lld\n", res);
    }
}