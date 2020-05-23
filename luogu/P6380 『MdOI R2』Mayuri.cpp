#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

const int MAXN = 1e5 + 5;
const int MAXM = 11;
const int INF = 0x7fffffff;

int dp[MAXN][MAXM];
int a,b,cnt;
char s[MAXN],res[MAXN];

int dfs(int idx,int remains){
    if(idx==b)return 1;
    if(dp[idx][remains]!=-1){
        return dp[idx][remains];
    }
    for (int i=0; i<10; i++) {
        if (idx==0 && i==0)continue;
        if (((remains*10+i)%a==0)==(s[idx]=='1')) {
            res[idx]=i;
            if (dfs(idx+1, (remains*10+i)%a)==1) {
                dp[idx][remains]=1;
                return 1;
            }
            
        }
    }
    dp[idx][remains]=0;
    return 0;
}

signed main(void)
{
//    freopen("input.txt", "r", stdin);
    cin >> a >> b >> s;
    memset(dp, -1, sizeof(dp));
    if (a==10 && s[0]=='1') {
        printf("%d\n",-1);
    }
    else{
        dfs(0, 0);
        for (int i=0; i<b; i++) {
            printf("%d",res[i]);
        }
        printf("\n");
    }

    return 0;
}
