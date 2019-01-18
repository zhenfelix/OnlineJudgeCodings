#include<cstdio>
#include<queue>
using namespace std;
#define maxn 15
struct Node{
	int key;
	Node *left;
	Node *right;
}*T;
bool HashTable[maxn]={false};
int l[maxn],r[maxn],n,num=0;
int find_root(){
	int i=0;
	while(HashTable[i]!=false)i++;
	return i;
}
Node* create(int index){
	Node *root=new Node;
	root->key=index;
	if(l[index]!=-1)root->left=create(l[index]);
	else root->left=NULL;
	if(r[index]!=-1)root->right=create(r[index]);
	else root->right=NULL;
	return root;
}
void invert(Node *root){
	if(root==NULL)return;
	Node *temp;
	temp=root->left;
	root->left=root->right;
	root->right=temp;
	invert(root->left);
	invert(root->right);
	return;
}
void bfs(){
	queue<Node*>q;
	q.push(T);
	while(!q.empty()){
		Node *temp=q.front();
		q.pop();
		num++;
		printf("%d",temp->key);
		if(num<n)printf(" ");
		else printf("\n");
		if(temp->left!=NULL)q.push(temp->left);
		if(temp->right!=NULL)q.push(temp->right);
	}
}
void inorder(Node *root){
	if(root==NULL)return;
	inorder(root->left);
	printf("%d",root->key);
	num++;
	if(num<n)printf(" ");
	inorder(root->right);
}
int main(){
	freopen("A1102.txt","r",stdin);
	char left,right;
	scanf("%d\n",&n);
	for(int i=0;i<n;i++){
		scanf("%c %c\n",&left,&right);
		if(left=='-')l[i]=-1;
		else{
			l[i]=left-'0';
			HashTable[l[i]]=true;
		}
		if(right=='-')r[i]=-1;
		else{
			r[i]=right-'0';
			HashTable[r[i]]=true;
		}
	}
	T=create(find_root());
	invert(T);
	bfs();
	num=0;
	inorder(T);
	return 0;
}
