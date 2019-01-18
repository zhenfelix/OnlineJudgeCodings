#include<cstdio>
#include<algorithm>
#include<vector>
#include<queue>
#include<cmath>
using namespace std;
#define maxn 1010
vector<int> ans,order;
int x[maxn],n;
struct Node{
	int data;
	Node *left,*right;
};
void insert(Node* &root,int data){
	if(root==NULL){
		root=new Node;
		root->data=data;
		root->left=root->right=NULL;
		return;
	}
	if(data<root->data)insert(root->left,data);
	else insert(root->right,data);
}
void bfs(Node *root){
	if(root==NULL)return;
	queue<Node*>q;
	q.push(root);
	while(!q.empty()){
		Node *temp=q.front();
		ans.push_back(temp->data);
		q.pop();
		if(temp->left!=NULL)q.push(temp->left);
		if(temp->right!=NULL)q.push(temp->right);
	}
	return;
}
void find_root(int a,int b){
	
	if(a==b){
		order.push_back(a);
		return;
	}
	else if(a>b)return;
	int count=0,temp=b-a+1;
	int size=temp;
	while(temp!=0){
		temp/=2;
		count++;
	}
	
	int r=size-pow(2,count-1)+1;
	int idx=r>pow(2,count-2)?pow(2,count-1):r+pow(2,count-2);
	order.push_back(a+idx-1);
	find_root(a,a+idx-2);
	find_root(a+idx,b);
	return;
}
int main(){
	freopen("A1064.txt","r",stdin);
	scanf("%d",&n);
	for(int i=0;i<n;i++)scanf("%d",&x[i]);
	sort(x,x+n);
	find_root(0,n-1);
	Node *root=NULL;
	for(int i=0;i<n;i++){
		int data=x[order[i]];
		insert(root,data);
	}
	bfs(root);
	for(int i=0;i<n;i++){
		printf("%d",ans[i]);
		if(i<n-1)printf(" ");
	}
	return 0;
}
