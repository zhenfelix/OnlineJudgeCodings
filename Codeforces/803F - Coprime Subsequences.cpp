#include <bits/stdc++.h>
using namespace std;
const int N=1e5+5;
const int mod=1e9+7;
typedef long long ll;
ll x,mu[N],p[N],cnt[N];
int main()
{
    int n;ll m=0;cin>>n;p[0]=1;mu[1]=1;
    for(int i=1;i<=n;i++)    cin>>x,m=max(m,x),p[i]=p[i-1]*2%mod,cnt[x]++;
    for(int i=1;i<=m;i++)
    {
        for(int j=2;j<=m/i;j++)
        {
            mu[i*j]-=mu[i];
        }
    }ll ans=0;
    for(int i=1;i<=m;i++)
    {
        int s=0;
        for(int j=1;j<=m/i;j++)
        {
            s+=cnt[i*j];
        }ans+=(mu[i]*(p[s]-1)%mod+mod)%mod;ans%=mod;
    }cout<<ans<<'\n';
    return 0;
}