#include<cstdio>
struct Node{
	int data;
	Node *left,*right;
};
const int maxn=50010;
int a[maxn],b[maxn],ans[maxn],n,count=0;
Node* build(int i,int j,int k,int l){
	Node *root=new Node;
	root->data=a[i];
	root->left=root->right=NULL;
	int num;
	for(num=k;num<=l;num++){
		if(b[num]==a[i])break;
	}
	if(num>k)root->left=build(i+1,i+num-k,k,num-1);
	if(num<l)root->right=build(i+num-k+1,j,num+1,l);
	return root;
}
void post_order(Node *root){
	if(root==NULL)return;
	post_order(root->left);
	post_order(root->right);
	ans[count++]=root->data;
	return;
}
int main(){
//	freopen("A1138.txt","r",stdin);
	scanf("%d",&n);
	for(int i=0;i<n;i++)scanf("%d",&a[i]);
	for(int i=0;i<n;i++)scanf("%d",&b[i]);
	Node *T=build(0,n-1,0,n-1);
	post_order(T);
	printf("%d",ans[0]);
	return 0;
}
