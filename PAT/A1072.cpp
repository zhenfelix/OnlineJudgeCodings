#include<cstdio>
#include<vector>
using namespace std;
const int nmax=1050;
const int mmax=20;
const int inf=1000000000;
int n,m,k,ds;
int G[nmax][nmax],d[mmax][nmax];
bool visit[nmax];
void init(){
	for(int i=1;i<=n+m;i++)visit[i]=false;
	return;
}
void dijkstra(int source){
	init();
	int idx=source-n;
	d[idx][source]=0;
	for(int i=1;i<=n+m;i++){
		int dmin=inf;
		int u=-1;
		for(int j=1;j<=n+m;j++){
			if(visit[j]==false&&d[idx][j]<dmin){
				u=j;
				dmin=d[idx][j];
			}
		}
		if(u==-1)return;
		visit[u]=true;
		for(int j=1;j<=n+m;j++){
			if(G[u][j]<inf&&visit[j]==false){
				if(d[idx][u]+G[u][j]<d[idx][j]){
					d[idx][j]=d[idx][u]+G[u][j];
				}
			}
		}
	}
}
bool ischar(char c){
	if(c=='G')return true;
	return false;
}
int main(){
	freopen("A1072.txt","r",stdin);
	scanf("%d%d%d%d",&n,&m,&k,&ds);
	for(int i=1;i<=n+m;i++){
		for(int j=1;j<=n+m;j++){
			G[i][j]=inf;
		}
	}
	for(int i=1;i<=m;i++){
		for(int j=1;j<=n+m;j++){
			d[i][j]=inf;
		}
	}
	
	for(int i=0;i<k;i++){
		int a,b,dis;
		char temp;
		getchar();
		scanf("%c",&temp);
		if(ischar(temp)){
			scanf("%d",&a);
			a+=n;
		}
		else{
			a=temp-'0';
		}
		
		getchar();
		
		scanf("%c",&temp);
		if(ischar(temp)){
			scanf("%d",&b);
			b+=n;
		}
		else{
			b=temp-'0';
		}
		scanf("%d",&dis);
		G[a][b]=dis;
		G[b][a]=dis;
		
	}
	
	for(int i=1;i<=m;i++){
		dijkstra(i+n);
	}
	int mark=-1,gd=0;
	double total=1000000000.0;
	for(int i=1;i<=m;i++){
		bool flag=true;
		int temp=inf;
		for(int j=1;j<=n;j++){
			if(d[i][j]>ds){
				flag=false;
				break;
			}
			if(d[i][j]<temp){
				temp=d[i][j];
			}
		}
		if(flag){
			double total_temp=0.0;
        		for(int cc=1;cc<=n;cc++)total_temp+=d[i][cc];
        		total_temp=total_temp/n;
        		total_temp=((int) (total_temp*100))%10>=5?total_temp+0.05:total_temp;
			if(temp>gd||(temp==gd&&total_temp<total)){
				gd=temp;
				mark=i;
				total=total_temp;
			}
			
		}
	}
	if(mark==-1)printf("No Solution\n");
	else{
//		double total=0.0;
//		for(int i=1;i<=n;i++)total+=d[mark][i];
//		total=total/n;
//		total=((int) (total*100))%10>=5?total+0.05:total;
		printf("G%d\n",mark);
		printf("%.1f %.1f\n",(double) gd,total);
	}
	return 0;
}
