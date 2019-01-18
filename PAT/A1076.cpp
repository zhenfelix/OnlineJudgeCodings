#include<cstdio>
#include<vector>
#include<queue>
using namespace std;
#define nmax 1010
vector<int> G[nmax];
queue<int> q;
int n,l,k,user[nmax]={0},num;
bool visit[nmax]={false};
void bfs(int root){
	int temp,v;
	q.push(root);
	user[root]=0;
	visit[root]=true;
	num=0;
	while(!q.empty()){
		temp=q.front();
		q.pop();
//		printf("%d ",temp);
		if(user[temp]>l)return;
		num++;
		for(int i=0;i<G[temp].size();i++){
			v=G[temp][i];
			if(visit[v]==false){
				q.push(v);
				user[v]=user[temp]+1;
				visit[v]=true;
			}
		}
		
	}
}
void query(int root){
	bfs(root);
	printf("%d\n",num-1);
	for(int i=1;i<=n;i++){
		visit[i]=false;
		user[i]=0;
	}
	while(!q.empty())q.pop();
}
int main(){
	freopen("A1076.txt","r",stdin);
	int m,temp;
	scanf("%d%d",&n,&l);
	for(int i=1;i<=n;i++){
		scanf("%d",&m);
		for(int j=0;j<m;j++){
			scanf("%d",&temp);
			G[temp].push_back(i);
		}
	}
	scanf("%d",&k);
	for(int i=0;i<k;i++){
		scanf("%d",&temp);
		query(temp);
	}
	return 0;
}
