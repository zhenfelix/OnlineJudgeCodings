#include<cstdio>
#include<vector>
using namespace std;
const int nmax=510;
const int inf=1000000000; 
struct Node{
	int id,dis,cost;
};
int n,m,s,t,d[nmax],c[nmax],pre[nmax];
vector<Node> G[nmax];
bool S[nmax]={false};
void init(){
	for(int i=0;i<n;i++){
		d[i]=inf;
		c[i]=inf;
	}
}
void dijkstra(int source){
	d[source]=0;
	c[source]=0;
	for(int i=0;i<n;i++){
		int dmin=inf;
		int u=-1;
		for(int j=0;j<n;j++){
			if(S[j]==false&&d[j]<dmin){
				dmin=d[j];
				u=j;
			}
		}
		if(u==-1)return;
		S[u]=true;
		for(int j=0;j<G[u].size();j++){
			//printf("%d\n",G[u][j].id);
			if(S[G[u][j].id]==false){
				if((G[u][j].dis+d[u]<d[j])||(G[u][j].dis+d[u]==d[j]&&G[u][j].cost+c[u]<c[j])){
					d[j]=G[u][j].dis+d[u];
					c[j]=G[u][j].cost+c[u];
					pre[j]=u;
				}
			}
		}
	}
}
void path_show(int city){
	if(city==s){
		printf("%d ",s);
	} 
	path_show(pre[city]);
	printf("%d ",city);
}
int main(){
	freopen("A1030.txt","r",stdin);
	scanf("%d%d%d%d",&n,&m,&s,&t);
	init();
	for(int i=0;i<m;i++){
		int a,b;
		struct Node temp;
		scanf("%d%d",&a,&b);
		scanf("%d%d",&temp.dis,&temp.cost);
		temp.id=b;
		G[a].push_back(temp);
		temp.id=a;
		G[b].push_back(temp);
	}
	dijkstra(s);
	for(int i=0;i<n;i++)printf("%d ",S[i]);
	printf("\n");
//	path_show(t);
	printf("%d %d",d[t],c[t]);
}
