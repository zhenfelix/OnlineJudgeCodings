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
char arr[maxn];
ll k, sz;
string s;
ll cnt[maxch];
// ll s[maxn], mx;

std::ostream &operator<<(std::ostream &stream,
                         vector<pci> &v)
{
    for (auto [ch,i] : v) stream << ch << ": " << i << " ";
    return stream;
}


void solve()
{
    scanf("%d%d%d\n", &n, &c, &q);
    scanf("%s\n", arr+1);
    lo[0] = 1, hi[0] = n;
    l[0] = 1, r[0] = n;
    for (int i = 1; i <= c; i++){
        scanf("%lld%lld\n", &l[i], &r[i]);
        sz = hi[i-1];
        lo[i] = sz+1, hi[i] = lo[i]+r[i]-l[i];
    }
    for (int i = 0; i < q; i++){
       scanf("%lld", &k);
       for (int j = c; j > 0; j--){
        if (lo[j] <= k && k <= hi[j]){
            k = l[j]+k-lo[j];
        }
       }
       printf("%c\n", arr[k]);
    }
    return;
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
        solve();
    }
}