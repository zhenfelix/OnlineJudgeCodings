#include<cstdio>
#include<vector>
using namespace std;
const int nmax=510;
const int inf=1000000000;
struct Node{
	int id,dis;
};
int n,m;
vector<Node> G[nmax];
int v[nmax],Tn[nmax],Tn_u[nmax],num[nmax]={0};
bool visit[nmax]={false};
void init(){
	for(int i=0;i<n;i++){
		v[i]=inf;
		Tn_u[i]=0;
	}
}
void dijkstra(int source){
	init();
	v[source]=0;
	num[source]=1;
	Tn_u[source]=Tn[source];
	for(int i=0;i<n;i++){
		int umin=inf,u;
		for(int j=0;j<n;j++){
			if(visit[j]==false&&v[j]<umin){
				u=j;
				umin=v[u];
			}
		}
		visit[u]=true;
		for(int j=0;j<G[u].size();j++){
			if(v[u]+G[u][j].dis<v[G[u][j].id]){
				v[G[u][j].id]=v[u]+G[u][j].dis;
				num[G[u][j].id]=num[u];
				Tn_u[G[u][j].id]=Tn_u[u]+Tn[G[u][j].id];
			}
			else if(v[u]+G[u][j].dis==v[G[u][j].id]){
				num[G[u][j].id]+=num[u];
				if(Tn_u[G[u][j].id]<Tn_u[u]+Tn[G[u][j].id]){
					Tn_u[G[u][j].id]=Tn_u[u]+Tn[G[u][j].id];
				}
			}
		}
	}
}
int main(){
	freopen("A1003.txt","r",stdin);
	int s1,s2,c1,c2,d;
	scanf("%d%d%d%d",&n,&m,&s1,&s2);
	for(int i=0;i<n;i++)scanf("%d",&Tn[i]);
	for(int i=0;i<m;i++){
		scanf("%d%d%d",&c1,&c2,&d);
		struct Node a,b;
		a.dis=d;a.id=c2;
		b.dis=d;b.id=c1;
		G[c1].push_back(a);
		G[c2].push_back(b);
	}
	dijkstra(s1);
	printf("%d %d",num[s2],Tn_u[s2]);
	return 0;
}
