
// #include <bits/stdc++.h>
#include <vector>
#include <algorithm>
#include <climits>
#include <iostream>
#include <unordered_map>
#include <cstring>
#include <queue>

using namespace std;
using ll = long long;
using pii = pair<int, int>;

const int inf = 0x3f3f3f3f;
const int maxn = 500005;

int t, n, m, tmp;
int a[maxn], b[maxn], idx[maxn], lo[maxn], hi[maxn];
// ll s[maxn], mx;

void solve()
{
    scanf("%d\n", &n);
    memset(a, 0, (n+1)*sizeof(int));
    memset(b, 0, (n + 1) * sizeof(int));
    memset(idx, 0, (n + 1) * sizeof(int));
    memset(lo, 0, (n + 1) * sizeof(int));
    memset(hi, 0, (n + 1) * sizeof(int));
    for (int i = 1; i <= n; i++){
        scanf("%d", &b[i]);
        idx[i] = i;
        lo[i] = i/(b[i]+1)+1;
        if (b[i] == 0) hi[i] = n;
        else hi[i] = i/b[i];
    }
    sort(idx + 1, idx + n + 1, [](int x, int y)
         { return lo[x] < lo[y]; });
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    int cur = 1;
    for (int i = 1; i <= n; i++) {
        while (cur <= n and lo[idx[cur]] <= i)
        {
            pq.push({hi[idx[cur]],idx[cur]});
            cur++;
        }
        auto [tmp, j] = pq.top();
        pq.pop();
        a[j] = i;
    }
    for (int i = 1; i <= n; i++) {
        printf("%d", a[i]);
        if (i < n) printf(" ");
        else printf("\n");
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
