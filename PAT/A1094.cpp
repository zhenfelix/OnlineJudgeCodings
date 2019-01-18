#include<cstdio>
#include<queue>
#include<vector>
using namespace std;
#define maxn 110
int ans=0,level;
struct Node{
	int level;
	vector<int>child;
}node[maxn];
void bfs(Node root){
	int now=1,count=0;
	queue<Node>q;
	root.level=1;
	q.push(root);
	while(!q.empty()){
		Node temp=q.front();
		q.pop();
		for(int i=0;i<temp.child.size();i++){
			node[temp.child[i]].level=temp.level+1;
			q.push(node[temp.child[i]]);
		}
		if(now==temp.level){
			count++;
			if(count>ans){
				ans=count;
				level=now;
			}
		}
		else{
			now++;
			count=1;
		}
	}
}
int main(){
	freopen("A1094.txt","r",stdin);
	int n,m;
	scanf("%d%d",&n,&m);
	for(int i=1;i<=m;i++){
		int idx,temp;
		scanf("%d%d",&idx,&temp);
		for(int j=0;j<temp;j++){
			int v;
			scanf("%d",&v);
			node[idx].child.push_back(v);
		}
	}
	bfs(node[1]);
	printf("%d %d",ans,level);
	return 0;
}
