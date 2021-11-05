
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
const int maxm = 5e2 + 10;
const int maxv = 1e4+10;

int dp[maxv], ndp[maxv], deq[maxv];
int cnt[maxm], vol[maxm], val[maxm];
int V, m;

void solve()
{
    char dummy;
    scanf("%d%d", &V, &m);
    getchar();
    for (int i = 0; i < m; i++){
        scanf("%d%d%d\n", &cnt[i], &vol[i], &val[i]);
    }
    for (int i = 0; i <= V; i++)
        dp[i] = -inf;
    dp[0] = 0;
    // memset(dp, 0, V * sizeof(int));
    for (int i = 0; i < m; i++){
        memset(ndp, 0, V*sizeof(int));
        for (int j = 0; j < vol[i] && j <= V; j++){
            int left = 0, right = -1;
            for (int k = 0; j+k*vol[i] <= V; k++){
                while (right >= left && dp[j + k * vol[i]] - k * val[i] > dp[j + deq[right] * vol[i]]-deq[right]*val[i]){
                    right--;
                }
                deq[++right] = k;
                if (deq[right]-deq[left] > cnt[i])
                    left++;
                ndp[j+k*vol[i]] = dp[j+deq[left]*vol[i]]-deq[left]*val[i]+k*val[i];
            }
        }
        swap(dp, ndp);
    }
    int res = 0;
    for (int j = 0; j <= V; j++)
        res = max(res, dp[j]);
    printf("%d\n", res);
}

int main()
{
    freopen("input", "r", stdin);
    solve();
}
