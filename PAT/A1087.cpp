#include<iostream>
#include<cstdio>
#include<map>
#include<vector>
#include<cstring>
using namespace std;
const int nmax=210;
const int inf=1000000000;
int n,k;
int cc=0,h_max=0,ha_max=0,h_temp=0,ha_temp=0;
int G[nmax][nmax],d[nmax],h[nmax]={0},num[nmax]={0};
vector<int> pre[nmax],path,path_temp;
bool visit[nmax]={false};
map<string,int> str2int;
map<int,string> int2str;
void init(){
	for(int i=0;i<n;i++){
		d[i]=inf;
		for(int j=0;j<n;j++){
			G[i][j]=inf;
		}
	}
}
void dijkstra(int source){
	
	d[source]=0;
	num[source]=1;
	for(int i=0;i<n;i++){
		int dmin=inf,u=-1;
		for(int j=0;j<n;j++){
			if(visit[j]==false&&d[j]<dmin){
				dmin=d[j];
				u=j;
			}
		}
		if(u==-1)return;
		visit[u]=true;
		for(int j=0;j<n;j++){
			if(visit[j]==false&&G[u][j]<inf){
				if(G[u][j]+d[u]<d[j]){
					d[j]=G[u][j]+d[u];
					num[j]=num[u];
					pre[j].clear();
					pre[j].push_back(u);
				}
				else if(G[u][j]+d[u]==d[j]){
					num[j]+=num[u];
					pre[j].push_back(u);
				}
			}
		}
	}
}
void dfs(int st){
	if(st==0){
		path_temp.push_back(st);
		h_temp+=h[st];
		ha_temp=h_temp/cc;
		if(h_temp>h_max||(h_temp==h_max&&ha_temp>ha_max)){
			path=path_temp;
			h_max=h_temp;
			ha_max=ha_temp;
		}
		h_temp-=h[st];
		path_temp.pop_back();
		return;
	}
	path_temp.push_back(st);
	cc++;
	h_temp+=h[st];
	for(int i=0;i<pre[st].size();i++){
		dfs(pre[st][i]);
	}
	cc--;
	h_temp-=h[st];
	path_temp.pop_back();
	return;
}
int main(){
	freopen("A1087.txt","r",stdin);
	int temp;
	string str1,str2;
	cin>>n>>k>>str1;
	init();
	str2int[str1]=0;int2str[0]=str1;
	for(int i=1;i<n;i++){
		cin>>str1>>temp;
		str2int[str1]=i;int2str[i]=str1;
		h[i]=temp;
	}
	for(int i=0;i<k;i++){
		cin>>str1>>str2>>temp;
		int a,b;
		a=str2int[str1];b=str2int[str2];
		G[a][b]=G[b][a]=temp;
	}
	int st=str2int["ROM"];
	dijkstra(0);
	dfs(st);
	printf("%d %d %d %d\n",num[st],d[st],h_max,ha_max);
	cout<<int2str[0];
	path.pop_back();
	for(int i=path.size()-1;i>=0;i--){
		cout<<"->"<<int2str[path[i]];
	}
}
