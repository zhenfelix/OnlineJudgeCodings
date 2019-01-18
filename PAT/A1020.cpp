#include<cstdio>
#include<queue>
using namespace std;
int a[35],b[35],num=0,n;
struct Node{
	int key;
	Node *left;
	Node *right;
};

Node* create(int a_left,int a_right,int b_left,int size){
	if(a_left>a_right)return NULL;
	int count=0;
	Node *root=new Node;
	root->key=a[a_right];
	while(b[b_left+count]!=a[a_right])count++;
	root->left=create(a_left,a_left+count-1,b_left,count);
	root->right=create(a_left+count,a_right-1,b_left+count+1,size-count-1);
	return root;
}
void bfs(Node *root){
	queue<Node*>q;
	q.push(root);
	while(!q.empty()){
		Node *now=q.front();
		q.pop();
		num++;
		printf("%d",now->key);
		if(num!=n)printf(" ");
		if(now->left!=NULL)q.push(now->left);
		if(now->right!=NULL)q.push(now->right);
	}
}
int main(){
	freopen("A1020.txt","r",stdin);
	scanf("%d",&n);
	for(int i=0;i<n;i++)scanf("%d",&a[i]);
	for(int i=0;i<n;i++)scanf("%d",&b[i]);
	Node *root=create(0,n-1,0,n);
	bfs(root);
	return 0;
}
