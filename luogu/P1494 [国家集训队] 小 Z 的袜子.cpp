#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
typedef long long LL;
const int maxn=50005;
int n,m,pos[maxn],c[maxn];
LL s[maxn],ans;
struct Data{
    int l,r,id;
    LL a,b;
}da[maxn];
bool cmp(const Data &a, const Data &b)
{
    if(pos[a.l]==pos[b.l])
        return a.r<b.r;
    return a.l<b.l;
}
bool cmp_id(const Data &a,const Data &b)
{
    return a.id<b.id;
}
void update(int p,int add)
{
    ans-=s[c[p]]*s[c[p]];
    s[c[p]]+=add;
    ans+=s[c[p]]*s[c[p]];
}
void solve()
{
    for(int i=1,l=1,r=0;i<=m;i++)
    {
        for(;r<da[i].r;r++)
            update(r+1,1);
        for(;r>da[i].r;r--)
            update(r,-1);
        for(;l<da[i].l;l++)
            update(l,-1);
        for(;l>da[i].l;l--)
            update(l-1,1);
        if(da[i].l==da[i].r)
        {
            da[i].a=0;
            da[i].b=1;
            continue;
        }
        da[i].a=ans-(da[i].r-da[i].l+1);
        da[i].b=(da[i].r-da[i].l+1)*1LL*(da[i].r-da[i].l);
        LL g=__gcd(da[i].a,da[i].b);
        da[i].a/=g;
        da[i].b/=g;
    }
}
int main()
{
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++)
        scanf("%d",&c[i]);
    int block=sqrt(n);
    for(int i=1;i<=n;i++)
        pos[i]=(i-1)/block+1;
    for(int i=1;i<=m;i++)
    {
        scanf("%d%d",&da[i].l,&da[i].r);
        da[i].id=i;
    }
    sort(da+1,da+m+1,cmp);
    solve();
    sort(da+1,da+m+1,cmp_id);
    for(int i=1;i<=m;i++)
        printf("%lld/%lld\n",da[i].a,da[i].b);
    return 0;
}