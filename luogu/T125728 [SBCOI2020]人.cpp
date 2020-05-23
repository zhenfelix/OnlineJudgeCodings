#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
//#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define N 110
#define Mod 998244353
int t,m,a,b;
ll dp[N][N][N];
int main(){
//    freopen("input.txt", "r", stdin);
    scanf("%d",&t);
//    scanf("%d %d %d",&n,&m,&q);
    memset(dp,0,sizeof(dp));
    for (m=0; m<=N-1; m++) {
        dp[m][0][0]=1;
        for (a=0; a<=m; a++) {
            dp[m][a][m-a]=1;
        }
    }
//    dp[0][0][0] = dp[1][0][0] = dp[1][0][1] = dp[1][1][0] = 1;
    for (m=2; m<=N-1; m++) {
//        dp[m][0][0]=1;
        for (b=1; b<m; b++) {
            dp[m][0][b]=dp[m-1][0][b]+dp[m-1][0][b-1];
            dp[m][0][b] %= Mod;
        }
        for (a=1; a<m; a++) {
            dp[m][a][0]=dp[m-1][a][0]+dp[m-1][a-1][0];
            dp[m][a][0] %= Mod;
        }
        for (a=1; a<m; a++) {
            for (b=1; b<m; b++) {
                dp[m][a][b]=dp[m-1][a][b]+dp[m-1][a-1][b]+dp[m-1][a][b-1]-dp[m-2][a-1][b-1]+Mod;
                dp[m][a][b] %= Mod;
            }
        }
    }
    while (t--) {
        scanf("%d %d %d",&m,&a,&b);
        printf("%lld\n",dp[m][a][b]);
    }
    return 0;
}
