#include<bits/stdc++.h>
#define INF 0x7f7f7f7f
#define MAXN 100005
using namespace std;

vector<int> g[MAXN];
int n,m,f[MAXN],mi[MAXN],c[MAXN];

void dfs(int x,int minx,int pre) {
    int flag=1; 
    minx=min(c[x],minx);
    if (mi[x]>minx) mi[x]=minx,flag=0;
    int maxx=max(f[pre],c[x]-minx);
    if (f[x]<maxx) f[x]=maxx,flag=0;
    if (flag) return;
    for (int i=0;i<g[x].size();i++) dfs(g[x][i],minx,x);
}

int main() {
    scanf("%d%d",&n,&m);
    for (int i=0;i<MAXN;i++) mi[i]=INF;
    for (int i=1;i<=n;i++) scanf("%d",&c[i]);
    for (int i=1;i<=m;i++) {
        int t1,t2,t3;
        scanf("%d%d%d",&t1,&t2,&t3);
        g[t1].push_back(t2);
        if (t3==2) g[t2].push_back(t1);
    }
    dfs(1,INF,0);
    printf("%d\n",f[n]);
    return 0;
}


#include <iostream>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

int a[100001],tb[100001],ta[100001];

vector<int> g[100001],gf[100001];

int main()
{
    int n,m;
    cin>>n>>m;
    for(int i=1;i<=n;++i)
    {
        cin>>a[i];
    }
    for(int i=1;i<=m;i++)
    {
        int x,y,z;
        cin>>x>>y>>z;
        g[x].push_back(y);
        gf[y].push_back(x);
        if(z==2)
        {
            g[y].push_back(x);
            gf[x].push_back(y);
        }
    }
    queue<int> q;
    q.push(1);
    memset(ta,127,sizeof(ta));
    ta[1]=2147483647;
    while(!q.empty())
    {
        int t=q.front();
        q.pop();
        ta[t]=min(ta[t],a[t]);
        int l=g[t].size();
        for(int i=0;i<l;i++)
        {
            if(ta[t]<ta[g[t][i]])
            {
                ta[g[t][i]]=ta[t];
                q.push(g[t][i]);
            }
        }
    }
    q.push(n);
    while(!q.empty())
    {
        int t=q.front();
        q.pop();
        tb[t]=max(tb[t],a[t]);
        int l=gf[t].size();
        for(int i=0;i<l;i++)
        {
            if(tb[t]>tb[gf[t][i]])
            {
                tb[gf[t][i]]=tb[t];
                q.push(gf[t][i]);
            }
        }
    }
    int ans=0;
    for(int i=1;i<=n;i++)
    {
        ans=max(ans,tb[i]-ta[i]);
    }
    cout<<ans;
    return 0;
}


#include<bits/stdc++.h>
using namespace std;
#define oo 1<<18;
const int maxn = 100010;
struct u {
    int v,len; 
};
int n, m, v[maxn], d[maxn*3+1];
vector<u> G[maxn*3+1];

void addedge(int x,int y) {
  G[x].push_back((u){y,0});
  G[x+n].push_back((u){y+n,0});//第二层图我从n+1到2n进行编号 
  G[x+2*n].push_back((u){y+2*n,0});//第三层图我从2*n+1到3*n进行编号 
  G[x].push_back((u){y+n,-v[x]});
  G[x+n].push_back((u){y+2*n,v[x]});
  return;
}

queue<int> Q;
bool inq[maxn*3+1];

void spfa() {
  for(int i = 1;i <= n;i++)    d[i] = -oo;
  d[1] = 0;
  inq[1] = true;
  Q.push(1);
  while(!Q.empty()) {
      int tp = Q.front(); Q.pop();
      inq[tp] = false;
      int len = G[tp].size();
      for(int i = 0;i < len;i++) {
          u x = G[tp][i];
          if(d[x.v] < d[tp] + x.len) {
              d[x.v] = d[tp] + x.len;
              if(inq[x.v] == false) {
                  Q.push(x.v);
          inq[x.v] = true;
              }
          } 
      }
  }
}

int main() {
//    freopen("d.txt","r",stdin);  调试用的 
    cin >> n >> m;
    for(int i = 1;i <= n;i++) cin >> v[i];
    for(int i = 1,x,y,z;i <= m;i++) {
        cin >> x >> y >> z;
        addedge(x,y);
        if(z == 2) addedge(y,x);
    }
    G[n].push_back((u){3*n+1,0});
    G[n*3].push_back((u){3*n+1,0});//超级终点是3*n+1编号 
    n = 3*n + 1; //把n改成超级终点的编号，方便spfa操作 

    spfa();
    cout << d[n] << endl;
    return 0;
}