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

const int maxn = 1005;
int T;
int a;

void solve()
{
    int n, m;
    cin >> n >> m;
    vector<ll> dp(2, LLONG_MIN);
    dp[0] = 0;
    for (int j = 0; j < n; j++)
    {
        ll mx = LLONG_MIN, mi = LLONG_MAX, cur = 0;
        for (int i = 0; i < m; i++)
        {
            cin >> a;
            cur += a;
            mx = max(mx, cur);
            mi = min(mi, cur);
        }
        vector<ll> cost = {mx, cur - mi};
        vector<ll> ndp(2, LLONG_MIN);
        for (int i = 0; i < 2; i++)
        {
            if (dp[i] == LLONG_MIN)
                continue;
            ndp[i] = max(ndp[i], dp[i]);
            ndp[1-i] = max(ndp[1-i], dp[i] + cur);
            ndp[i] = max(ndp[i], dp[i] + cost[i]);
        }
        swap(dp, ndp);
    }
    cout << max(dp[0], dp[1]) << endl;
}

int main()
{
    // freopen("input", "r", stdin);
    cin >> T;
    while (T--)
    {
        solve();
    }
}