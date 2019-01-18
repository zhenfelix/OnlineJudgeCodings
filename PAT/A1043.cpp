#include<cstdio>
#include<vector>
using namespace std;
vector<int> origin,pre,preM,post,postM;
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
void preorder(Node *root){
	if(root==NULL)return;
	pre.push_back(root->data);
	preorder(root->left);
	preorder(root->right);
}
void preorderM(Node *root){
	if(root==NULL)return;
	preM.push_back(root->data);
	preorderM(root->right);
	preorderM(root->left);
}
void postorder(Node *root){
	if(root==NULL)return;
	postorder(root->left);
	postorder(root->right);
	post.push_back(root->data);
}
void postorderM(Node *root){
	if(root==NULL)return;
	postorderM(root->right);
	postorderM(root->left);
	postM.push_back(root->data);
}
int main(){
	//freopen("A1043.txt","r",stdin);
	int n,temp;
	Node *root=NULL;
	scanf("%d",&n);
	
	for(int i=0;i<n;i++){
		scanf("%d",&temp);
		origin.push_back(temp);
		
		insert(root,temp);
	}
	preorder(root);preorderM(root);
	postorder(root);postorderM(root);
	
	if(pre==origin){
		printf("YES\n");
		for(int i=0;i<post.size();i++){
			printf("%d",post[i]);
			if(i<post.size()-1)printf(" ");
		}
	}
	else if(preM==origin){
		printf("YES\n");
		for(int i=0;i<postM.size();i++){
			printf("%d",postM[i]);
			if(i<postM.size()-1)printf(" ");
		}
	}
	else printf("NO\n");
	return 0;
}
