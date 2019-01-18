#include<cstdio>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;
#define maxn 110
int a[maxn],index=0;
vector<int> ans;
struct Node{
	int data;
	int left,right;
}node[maxn];
void inorder(int root){
	if(root==-1)return;
	inorder(node[root].left);
	node[root].data=a[index++];
	inorder(node[root].right);
}
void bfs(int root){
	queue<int> q;
	q.push(root);
	while(!q.empty()){
		int temp=q.front();
		ans.push_back(node[temp].data);
		q.pop();
		if(node[temp].left==-1);
		else q.push(node[temp].left);
		if(node[temp].right==-1);
		else q.push(node[temp].right);
	}
}
int main(){
	freopen("A1099.txt","r",stdin);
	int n,x,y;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		scanf("%d%d",&x,&y);
		node[i].left=x;
		node[i].right=y;
	}
	for(int i=0;i<n;i++)scanf("%d",&a[i]);
	sort(a,a+n);
	inorder(0);
	bfs(0);
	for(int i=0;i<n;i++){
		printf("%d",ans[i]);
		if(i<n-1)printf(" ");
	}
	return 0;
}
