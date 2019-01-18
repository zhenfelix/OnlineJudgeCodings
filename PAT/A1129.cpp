#include<cstdio>
#include<map>
using namespace std;
const int nmax=50010;
map<int,int> G;
int n,k;
struct Node{
	int item;
	int num=0;
}node[nmax];
bool cmp(int a,int b){
	if(node[a].num!=node[b].num)return node[b].num>node[a].num;
	else return node[b].item<node[a].item;
}
void swap(int a,int b){
	Node temp;
	temp=node[b];
	node[b]=node[a];
	node[a]=temp;
	G[node[b].item]=b;
	G[node[a].item]=a;
}
int main(){
	scanf("%d%d",&n,&k);
	int temp,p=1;
	scanf("%d",&temp);
	node[0].item=temp;
	node[0].num++;
	G[temp]=0;
	for(int i=1;i<n;i++){
		scanf("%d",&temp);
		printf("%d:",temp);
		for(int j=0;j<k&&node[j].num!=0;j++)printf(" %d",node[j].item);
		printf("\n");
		if(G.find(temp)==G.end()){
			G[temp]=p;
			node[G[temp]].item=temp;
			p++;
		}
		node[G[temp]].num++;
		int id=G[temp];
		while(cmp(node[id-1],node[id])&&id>0){
			swap(id-1,id);
			id--;
		}
	}
}
