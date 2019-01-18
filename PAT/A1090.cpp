#include<cstdio>
#include<queue>
#include<vector>
#include<cmath>
using namespace std;
#define maxn 100010
int count=0,ans=0;
struct Node{
	int level;
	vector<int>child;
}node[maxn];
void bfs(Node root){
	queue<Node>q;
	q.push(root);
	while(!q.empty()){
		Node temp=q.front();
		q.pop();
		for(int i=0;i<temp.child.size();i++){
			node[temp.child[i]].level=temp.level+1;
			q.push(node[temp.child[i]]);
		}
		if(temp.child.empty()){
			
			if(temp.level>ans){
				count=1;
				ans=temp.level;
			}
			else if(temp.level==ans)count++;
		}
	}
}
int main(){
	//freopen("A1090.txt","r",stdin);
	int n,temp,root;
	double p,r;
	scanf("%d%lf%lf",&n,&p,&r);
	r/=100.0;r+=1;
	for(int i=0;i<n;i++){
		scanf("%d",&temp);
		if(temp==-1)node[i].level=0,root=i;
		else{
			node[temp].child.push_back(i);
		}
	}
	
	bfs(node[root]);
	printf("%.2f %d",pow(r,(double)(ans))*p,count);
}
