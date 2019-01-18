#include<cstdio>
#include<cstring>
#include<stack>
using namespace std;
int a[35],b[35],n,sum=0;
struct Node{
	int key;
	Node *left;
	Node *right;
};
stack<int>s;
Node *create(int l1,int r1,int l2,int r2){
	if(r1<l1)return NULL;
	int count=0;
	Node *root=new Node;
	root->key=a[l1];
	while(b[l2+count]!=a[l1])count++;
	root->left=create(l1+1,l1+count,l2,l2+count-1);
	root->right=create(l1+count+1,r1,l2+count+1,r2);
	return root;
}
void postorder(Node *root){
	if(root==NULL)return;
	postorder(root->left);
	postorder(root->right);
	printf("%d",root->key);
	sum++;
	if(sum!=n)printf(" ");
	return;
}
int main(){
	freopen("A1086.txt","r",stdin);
	int x=0,y=0,temp;
	char str[5];
	scanf("%d",&n);
	for(int i=0;i<2*n;i++){
		scanf("%s",str);
		if(strcmp(str,"Push")==0){
			scanf("%d",&temp);
			s.push(temp);
			a[x++]=temp;
		}
		else{
			temp=s.top();
			s.pop();
			b[y++]=temp;
		}
	}
	Node *root=create(0,n-1,0,n-1);
	postorder(root);
	//printf("%d\n",root->left->right->key);
	return 0;
}
