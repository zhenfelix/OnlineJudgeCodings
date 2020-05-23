#include <bits/stdc++.h>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
typedef long long ll;
#define N 100010
ll degree[N],n,m,q,a,b,start,enden;
vector<ll> graph[N];
int main(){
//    freopen("input.txt", "r", stdin);
    scanf("%lld %lld %lld",&n,&m,&q);
//    scanf("%d %d %d",&n,&m,&q);
    memset(degree,0,sizeof(degree));
    for (int i=0; i<m; i++) {
        scanf("%lld %lld",&a,&b);
        graph[b].push_back(a);
        degree[a] += 1;
    }
    for (int i=0; i<q; i++) {
        scanf("%lld %lld",&start,&enden);
        ll cnt[N];
        int dp[N];
        memset(cnt,0,sizeof(cnt));
        memset(dp, 0, sizeof(dp));
        queue<ll> q;
        for (int j=1; j<=n; j++) {
            if (degree[j]==0 || j==enden) {
                dp[j] = -1;
                q.push(j);
            }
        }
        
        while (!q.empty()) {
            ll cur=q.front();
            q.pop();
            for (auto nxt: graph[cur]) {
                if (dp[nxt]!=0)continue;
                if (dp[cur]==-1) {
                    dp[nxt]=1;
                    q.push(nxt);
                }
                else{
                    cnt[nxt]++;
                    if (cnt[nxt]==degree[nxt]) {
                        dp[nxt]=-1;
                        q.push(nxt);
                    }
                }
            }
        }
        printf("%d\n",dp[start]);
    }

    return 0;
}
