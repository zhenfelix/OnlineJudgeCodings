// Problem: D. Small GCD
// Contest: Codeforces - Codeforces Round 911 (Div. 2)
// URL: https://codeforces.com/contest/1900/problem/D
// Memory Limit: 256 MB
// Time Limit: 2000 ms
// 
// Powered by CP Editor (https://cpeditor.org)

#include <bits/stdc++.h>
#define INF 0x7fffffff
#define MAXN 100005
#define eps 1e-9
#define foru(a,b,c) for(int a=b;a<=c;a++)
#define RT return 0;
#define LL long long
#define LXF int
#define RIN rin()
#define HH printf("\n")
#define fi first
#define se second
using namespace std;
inline LXF rin(){
    LXF x=0,w=1;
    char ch=0;
    while(ch<'0'||ch>'9'){ 
    if(ch=='-') w=-1;
    ch=getchar();
    }
    while(ch>='0'&&ch<='9'){
    x=x*10+(ch-'0');
    ch=getchar();
    }
    return x*w;
}
int n;
int a[MAXN];
LL ans,sum;
vector<int> d[MAXN];
LL ct[MAXN];
void dfs(int i,int j){
    if(j==d[i].size())  return ;
    sum+=(LL)d[i][j]*ct[d[i][j]];
    // cout<<i<<' '<<d[i][j]<<' '<<ct[d[i][j]]<<endl;
    // if(d[i][j]*ct[d[i][j]])  cout<<"+"<<d[i][j]*ct[d[i][j]]<<endl;
    LL res=ct[d[i][j]];
    for(auto x:d[d[i][j]]){
        ct[x]-=res;
        // cout<<' '<<x<<' '<<ct[x]<<endl;
    }
    dfs(i,j+1);
    for(auto x:d[d[i][j]]){
        ct[x]+=res;
    }
}
signed main(){
    for(int i=100000;i>=1;i--){
        for(int j=i;j<=100000;j+=i){
            d[j].push_back(i);
        }
    }
    int T=RIN;
    while(T--){
        foru(i,1,100000)    ct[i]=0;
        n=RIN;
        ans=0;
        foru(i,1,n){
            a[i]=RIN;
        }
        sort(a+1,a+1+n);
        for(int i=1;i<=n;i++){
            sum=0;
            dfs(a[i],0);
            for(auto x:d[a[i]]){
                ct[x]++;
            }
            // for(int j=1;j<i;j++){
                // sum+=__gcd(a[i],a[j]);
            // }
            // cout<<sum<<endl;
            ans=(ans+sum*(LL)(n-i));
        }
        cout<<ans<<endl;
        // break;
    }
    return 0;
}