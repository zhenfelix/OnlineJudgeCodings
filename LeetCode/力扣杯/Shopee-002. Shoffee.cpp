#include<bits/stdc++.h>
using namespace std;
int N, K;
int V[100001];
long long res = 0;
int t[100001];
void solve(int l, int r) {
    if(l == r)
        return;
    int m = l + (r - l) / 2;
    solve(l, m);
    solve(m + 1, r);
    int i = l, j = m + 1, k = l;
    while(i <= m && j <= r) {
        if(V[i] <= V[j]) {
            res += r - j + 1;
            t[k++] = V[i++];
        }
        else
            t[k++] = V[j++];
    }
    while(i <= m)
        t[k++] = V[i++];
    while(j <= r)
        t[k++] = V[j++];
    for(int i = l; i <= r; i++)
        V[i] = t[i];
}
int main () {
    scanf("%d %d", &N, &K);
    for(int i = 1; i <= N; i++) {
        scanf("%d", &V[i]);
        V[i] -= K;
    }
    V[0] = 0;
    for(int i = 1; i <= N; i++)
        V[i] += V[i - 1];
    solve(0, N);
    printf("%lld\n", res);
}



#include <bits/stdc++.h>

using namespace std;

using ll = long long;

auto io_sync_off = []()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}();

const int maxn = 100005;
int T;
int a;
ll arr[maxn];
int tree[maxn];
set<ll> seen;
map<ll,int> mp;

int query(int x){
    int cnt = 0;
    while (x){
        cnt += tree[x];
        x -= (x&-x);
    }
    return cnt;
}

void update(int x){
    while (x < maxn){
        tree[x]++;
        x += (x&-x);
    }

}

void solve()
{
    int n, k;
    cin >> n >> k;
    seen.insert(k);
    ll s = 0;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        s += arr[i];
        arr[i] = s;
        seen.insert(arr[i]-i*k);
    }
    int cnt = 1;
    for (auto it = seen.begin(); it != seen.end(); it++,cnt++) mp[*it] = cnt;
    ll ans = 0;
    update(mp[k]);
    for (int i = 0; i < n; i++){
        int cc = query(mp[arr[i]-i*k]);
        ans += cc;
        update(mp[arr[i]-i*k]);
    }
    cout << ans << endl;
}

int main()
{
    // freopen("input", "r", stdin);
    // cin >> T;
    T = 1;
    while (T--)
    {
        solve();
    }
}