#include<cstdio>
#include<vector>
#include<queue>
using namespace std;
#define nmax 1010
int n,m,k;
vector<int> edge[nmax];
queue<int> q1,q2;
bool visit[nmax]={false};
void dfs(int node){
	visit[node]=true;
	for(int i=0;i<edge[node].size();i++){
		
		if(visit[edge[node][i]]==false){
			dfs(edge[node][i]);
		}
	}
}
int dfs_main(){
	int num=0;
	for(int i=1;i<=n;i++){
		if(visit[i]==false){
			dfs(i);
			num++;
		}
	}
	return num;
}
void query(int c){
	vector<int>::iterator it;
	int a,b;
	while(!q1.empty()){
		a=q1.front();q1.pop();
		b=q2.front();q2.pop();
		edge[a].push_back(b);
		edge[b].push_back(a);
	}
	while(edge[c].size()>0){
		int temp=edge[c][0];
		edge[c].erase(edge[c].begin());
		for(it=edge[temp].begin();it!=edge[temp].end();it++){
			if(*it==c){
				edge[temp].erase(it);
				break;
			}
		}
		q1.push(c);
		q2.push(temp);
	}
	printf("%d\n",dfs_main()-2);
	for(int i=1;i<=n;i++)visit[i]=false;
}
int main(){
	//freopen("A1013.txt","r",stdin);
	int a,b;
	scanf("%d%d%d",&n,&m,&k);
	
	for(int i=0;i<m;i++){
		scanf("%d%d",&a,&b);
		edge[a].push_back(b);
		edge[b].push_back(a);
	}
	
//	printf("%d\n",dfs_main()-1);
	int temp;
	for(int i=0;i<k;i++){
		scanf("%d",&temp);
		query(temp);
	}
}
