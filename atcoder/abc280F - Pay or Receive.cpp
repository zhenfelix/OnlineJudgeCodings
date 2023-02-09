#include<bits/stdc++.h>
#include<atcoder/all>
using namespace std;
const long long INF=(long long)1e18;

int main(){
    int n,m,q;
    cin >> n >> m >> q;
    
    atcoder::dsu d(n);
    
    vector<vector<array<int,2>>>G(n);
    for(int i=0;i<m;i++){
        int a,b,c;
        cin >> a >> b >> c;
        a--,b--;
        d.merge(a,b);
        G[a].push_back({b,c});
        G[b].push_back({a,-c});
    }
    
    vector<long long>dist(n,INF);
    vector<bool>negative_loop(n);
    
    for(int i=0;i<n;i++)if(d.leader(i)==i){
        //bfs
        queue<int>q;
        dist[i]=0;
        q.push(i);
        while(!q.empty()){
            int v=q.front();q.pop();
            for(auto[vv,c]:G[v]){
                if(dist[vv]==INF){
                    dist[vv]=dist[v]+c;
                    q.push(vv);
                }else{
                    if(dist[vv]!=dist[v]+c)negative_loop[i]=true;
                }
            }
        }
    }
    
    for(int i=0;i<q;i++){
        int x,y;
        cin >> x >> y;
        x--,y--;
        if(!d.same(x,y)){
            cout << "nan" << endl;
        }else if(negative_loop[d.leader(x)]){
            cout << "inf" << endl;
        }else{
            cout << dist[y]-dist[x] << endl;
        }
    }
}
