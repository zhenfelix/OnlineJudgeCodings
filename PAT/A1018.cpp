#include<cstdio>
#include<vector>
using namespace std;
const int inf=1000000000;
const int nmax=510;
int n,m,cmax,c[nmax],d[nmax],remain_min=inf,need_min=inf;
int G[nmax][nmax];
vector<int> pre[nmax],path,path_temp;
bool S[nmax]={false};
void init(){
	for(int i=0;i<=n;i++){
		d[i]=inf;
		for(int j=0;j<=n;j++){
			G[i][j]=inf;
		}
	}
}
void dijkstra(int source){
	d[source]=0;
	for(int i=0;i<=n;i++){
		int u=-1,dmin=inf;
		for(int j=0;j<=n;j++){
			if(d[j]<dmin&&S[j]==false){
				dmin=d[j];
				u=j;
			}
		}
		if(u==-1)return;
		S[u]=true;
		for(int j=0;j<=n;j++){
			if(S[j]==false&&G[u][j]<inf){
				int delta=cmax/2-c[j];
				if(d[u]+G[u][j]<d[j]){
					d[j]=d[u]+G[u][j];
			    	pre[j].clear();
			    	pre[j].push_back(u);

				}
				else if(d[u]+G[u][j]==d[j]){
						pre[j].push_back(u);
				}
		}
		}
	}
}
void dfs(int v){
	if(v==0){
		//path_temp.push_back(v);
		int need=0,remain=0;
		for(int i=path_temp.size()-1;i>=0;i--){
			int temp=c[path_temp[i]]+remain;
			need=temp>0?need:-temp+need;
			remain=temp>0?temp:0;
		} 
		if((need<need_min)||(need==need_min&&remain<remain_min)){
			need_min=need;
			remain_min=remain;
			path=path_temp;
		}
		//path_temp.pop_back();
		return;
	}
	path_temp.push_back(v);
	for(int i=0;i<pre[v].size();i++){
		dfs(pre[v][i]);
	}
	path_temp.pop_back();
	return;
}
void path_show(){
	printf("0");
	for(int i=path.size()-1;i>=0;i--)printf("->%d",path[i]);
	return;
}
int main(){
	freopen("A1018.txt","r",stdin);
	int sp;
	scanf("%d%d%d%d",&cmax,&n,&sp,&m);
	init();//initialzation after updating the value of n
	for(int i=1;i<=n;i++){
		scanf("%d",&c[i]);
		c[i]=c[i]-cmax/2;//c[i]>0:remain
	}
	for(int i=0;i<m;i++){
		int a,b;
		scanf("%d%d",&a,&b);
		scanf("%d",&G[a][b]);
		G[b][a]=G[a][b];
	}
	dijkstra(0);
	dfs(sp);
	printf("%d ",need_min);
	path_show();
	printf(" %d",remain_min);
	return 0;
}
