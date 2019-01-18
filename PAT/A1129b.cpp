#include<cstdio>
#include<map>
using namespace std;
const int nmax=50010;
int G[nmax];
int n,k;
struct Node{
	int item;
	int num=0;
}node[nmax];
bool cmp(int a,int b){
	if(node[a].num!=node[b].num)return node[b].num>node[a].num;
	else return node[b].item<node[a].item;
}
void Swap(int a,int b){
	Node temp;
	temp=node[b];
	node[b]=node[a];
	node[a]=temp;
	G[node[b].item]=b;
	G[node[a].item]=a;
}
int binsearch(int left,int right,int id){
	if(left==right){
		if(cmp(left,id))return left;
		else return left+1;
	}
	int mid=(left+right)/2;
	if(cmp(mid,id)){
		return binsearch(left,mid,id);
	}
	else{
		return binsearch(mid+1,right,id);
	}
}
int main(){
	freopen("A1129.txt","r",stdin);
	scanf("%d%d",&n,&k);
	fill(G,G+n,-1);
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
		if(G[temp]==-1){
			G[temp]=p;
			node[G[temp]].item=temp;
			p++;
		}
		node[G[temp]].num++;
		int id=G[temp];
//		printf("id=%d\n",id);
		int ans=0;
		if(id>0)ans=binsearch(0,id-1,id);
		for(int j=id;j>=ans+1;j--){
			Swap(j-1,j);
		}
//		printf("id=%d ans=%d\n",id,ans);

//		Swap(ans,id);
//		while(cmp(id-1,id)&&id>0){
//			Swap(id-1,id);
//			id--;
//		}
	}
}
