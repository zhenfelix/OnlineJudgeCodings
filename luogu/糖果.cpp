#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

const int MAXN = 1e6 + 5;
const int INF = 0x7fffffff;

vector<int> g[MAXN];
int n,m,a,b,people[MAXN],power[MAXN],depth[MAXN];

void dfs(int cur, int parent, int d){
    if(people[cur]==1){
        power[cur]=cur;
        depth[cur]=d;
        return;
    }
    power[cur]=INF;depth[cur]=INF;
    for(auto nxt: g[cur]){
        if(nxt==parent)continue;
        dfs(nxt, cur, d+1);
        if ((depth[nxt]<depth[cur])||(depth[nxt]==depth[cur] && power[nxt]<power[cur])) {
            depth[cur]=depth[nxt];
            power[cur]=power[nxt];
        }
    }
    return;
}


signed main(void)
{
//    freopen("input.txt", "r", stdin);
    memset(people, 0, sizeof(people));
    memset(power, 0, sizeof(power));
    memset(depth, 0, sizeof(depth));
    scanf("%d %d", &n, &m);
    for (int i=1; i<=n-1; i++) {
        scanf("%d %d",&a,&b);
        g[a].push_back(b);
        g[b].push_back(a);
    }
    for (int i=0; i<m; i++) {
        int p;
        scanf("%d",&p);
        people[p]=1;
    }
    dfs(1,0,0);
    printf("%d\n",power[1]);
    
    return 0;
}
