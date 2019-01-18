#include<cstdio>
#include<vector>
#include<stack>
#include<algorithm>
using namespace std;
#define maxn 110
vector<int>node[maxn];
stack<int>ans[maxn],temp;
int n,m,s,w[maxn],cnt=0,sum;
void dfs(int root){
	if(node[root].empty()){
		if(sum==s){
			ans[cnt]=temp;
			cnt++;
		}
		return;
	}
	else if(sum>s){
		return;
	}
	for(int i=0;i<node[root].size();i++){
		int child=node[root][i];
		sum+=w[child];
		temp.push(w[child]);
		dfs(child);
		temp.pop();
		sum-=w[child];
	}
	
}
bool cmp(stack<int> a,stack<int> b){
	int x,y;
	while(!a.empty()||!b.empty()){
		x=a.top(),y=b.top();
		a.pop(),b.pop();
		if(x>y)return true;
		else if(x<y)return false;
	}
	return false;
}
int main(){
	freopen("A1053.txt","r",stdin);
	scanf("%d%d%d",&n,&m,&s);
	for(int i=0;i<n;i++)scanf("%d",&w[i]);
	for(int i=0;i<m;i++){
		int idx,num;
		scanf("%d%d",&idx,&num);
		for(int j=0;j<num;j++){
			int temp;
			scanf("%d",&temp);
			node[idx].push_back(temp);
		}
	}
	sum=w[0];
	temp.push(w[0]);
	dfs(0);
	for(int i=0;i<cnt;i++){
		stack<int> cup;
		int tt;
		while(!ans[i].empty()){
			tt=ans[i].top();
			ans[i].pop();
			cup.push(tt);
		}
		ans[i]=cup;
	}
	sort(ans,ans+cnt,cmp);
	for(int i=0;i<cnt;i++){
		printf("%d",ans[i].top());
		ans[i].pop();
		while(!ans[i].empty()){
			printf(" %d",ans[i].top());
			ans[i].pop();
		}
		printf("\n");
	}
	return 0;
}
