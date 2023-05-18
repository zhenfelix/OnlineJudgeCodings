#include <bits/stdc++.h>
using namespace std;

int dp[101][101][2][2]{};
void solve(){
    int n;
    cin>>n;
    vector<int>v(n);
    int o=0,e=0;
    for(int i=0;i<n;i++) {
        cin>>v[i];
        o+=(v[i]&1);
    }
    e=n-o;
    memset(dp,-1,sizeof(dp));
    auto dfs=[&](auto dfs,int odd,int even,int sta,int u)->int {
        if(odd==0&&even==0) return !(sta^u);
        if(dp[odd][even][sta][u]!=-1) return dp[odd][even][sta][u];
        int res=0;
        if(odd>0) res|=!dfs(dfs,odd-1,even,sta^1^u,!u);
        if(even>0) res|=!dfs(dfs,odd,even-1,sta,!u);
        dp[odd][even][sta][u]=res;
        return res;
    };
    int f=dfs(dfs,o,e,0,0);
    if(f) cout<<"Alice"<<endl;
    else cout<<"Bob"<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    // freopen("contests/input","r",stdin);
    int t;
    cin>>t;
    while(t--){
        solve();
    }
    cout.flush();
    return 0;
}
