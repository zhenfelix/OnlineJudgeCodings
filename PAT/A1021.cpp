#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
#define nmax 10010
int n,D,father[nmax];
vector<int> edge[nmax];
vector<int> temp,ans;

void init(){
	for(int i=1;i<=n;i++)father[i]=i;
}
int findroot(int x){
	if(father[x]==x)return x;
	int temp=findroot(father[x]);
	father[x]=temp;
	return temp;
}
void unite(int x, int y){
	int fx,fy;
	fx=findroot(x);
	fy=findroot(y);
	if(fx!=fy)father[fx]=fy;
}
void dfs(int v,int depth,int pre){
	if(depth>D){
		D=depth;
		temp.clear();
		temp.push_back(v);
	}
	else if(depth==D){
		temp.push_back(v);
	}
	for(int i=0;i<edge[v].size();i++){
		if(edge[v][i]!=pre){
			dfs(edge[v][i],depth+1,v);
		}
	}
}
int main(){
	freopen("A1021.txt","r",stdin);
	scanf("%d",&n);
	init();
	int a,b;
	for(int i=0;i<n-1;i++){
		scanf("%d%d",&a,&b);
		edge[a].push_back(b);
		edge[b].push_back(a);
		unite(a,b);
	}
	int block=0;
	for(int i=1;i<=n;i++){
		if(father[i]==i)block++;
	}
	if(block>1)printf("Error: %d components\n",block);
	else{
		D=-1;
		dfs(1,0,-1);
		ans=temp;
		D=-1;
		dfs(ans[0],0,-1);
		for(int i=0;i<temp.size();i++)ans.push_back(temp[i]);
		sort(ans.begin(),ans.end());
		printf("%d\n",ans[0]);
		for(int i=1;i<ans.size();i++){
			if(ans[i]!=ans[i-1])printf("%d\n",ans[i]);
		}
	}
	return 0;
}
