#include<cstdio>
#include<vector>
#include<queue>
using namespace std;
#define maxn 110
vector<int>node[maxn];
int count[maxn]={0},max_level=1;
void dfs(int idx,int level){
	if(node[idx].empty()){
		count[level]++;
		if(level>max_level)max_level=level;
		return;
	}
	for(int i=0;i<node[idx].size();i++)dfs(node[idx][i],level+1);
	return;
}
int main(){
	freopen("A1004.txt","r",stdin);
	int n,m;
	scanf("%d%d",&n,&m);
	for(int i=0;i<m;i++){
		int id,k;
		scanf("%d%d",&id,&k);
		for(int j=0;j<k;j++){
			int temp;
			scanf("%d",&temp);
			node[id].push_back(temp);
		}
	}
	dfs(1,1);
	for(int i=1;i<=max_level;i++){
		printf("%d",count[i]);
		if(i<max_level)printf(" ");
	}
	return 0;
}
