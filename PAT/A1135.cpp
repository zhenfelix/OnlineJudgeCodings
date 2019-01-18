#include<cstdio>
#include<cmath>
using namespace std;
const int nmax=40;
bool flag=true;
struct Node{
	int data;
	int left,right;
}node[nmax];
void tree(int root,int end){
	int i=root+1;
	if(i>=end){
		node[root].left=-1;
		node[root].right=-1;
		return;
	}
	while(i<end){
		int temp=abs(node[i].data);
		if(temp>=abs(node[root].data))break;
		i++;
	}
	if(i>root+1){
		node[root].left=root+1;
    	tree(node[root].left,i);
	}
	else{
		node[root].left=-1;
	}
	if(i<end){
		node[root].right=i;
    	tree(node[root].right,end);  
	}
	else{
		node[root].right=-1;
	}
	return;
}
void preorder(int root,int pre){
	if(root==-1)return;
	if(pre<0&&node[root].data<0)flag=false;
	preorder(node[root].left,node[root].data);
	preorder(node[root].right,node[root].data);
	return;
}
int main(){
	//freopen("d.txt","r",stdin);
	int k,n;
	scanf("%d",&k);
	
	for(int i=0;i<k;i++){
		scanf("%d",&n);
		for(int j=0;j<n;j++){
			scanf("%d",&node[j].data);
		}
		tree(0,n);
		flag=true;
		preorder(0,-1);
		if(flag)printf("Yes\n");
		else printf("No\n");
		
	}
}
