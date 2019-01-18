#include<cstdio>
#include<vector>
#include<cmath>
using namespace std;
#define maxn 100010
int ans=maxn,count=0;
vector<int>child[maxn];
void dfs(int idx,int level){
	if(child[idx].empty()){
		if(level<ans){
			ans=level;
			count=1;
		}
		else if(level==ans)count++;
	}
	for(int i=0;i<child[idx].size();i++)dfs(child[idx][i],level+1);
}
int main(){
	freopen("A1106.txt","r",stdin);
	int n;
	double p,r;
	scanf("%d%lf%lf",&n,&p,&r);
	r/=100;r+=1;
	for(int i=0;i<n;i++){
		int temp;
		scanf("%d",&temp);
		for(int j=0;j<temp;j++){
			int v;
			scanf("%d",&v);
			child[i].push_back(v);
		}
	}
	dfs(0,0);
	printf("%.4f %d",pow(r,ans)*p,count);
	return 0;
}
