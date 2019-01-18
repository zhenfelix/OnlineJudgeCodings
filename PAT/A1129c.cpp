#include<cstdio>
#include<map>
using namespace std;
const int nmax=50010;
int G[nmax],index2node[nmax];
int n,k;
struct Node{
	int item;
	int num=0;
	int rank=-1;
}node[nmax];
bool cmp(int a,int b){
	if(node[index2node[a]].num!=node[index2node[b]].num)return node[index2node[b]].num>node[index2node[a]].num;
	else return node[index2node[b]].item<node[index2node[a]].item;
}
void Swap(int a,int b){
	int temp;
	node[index2node[b]].rank=a;
	node[index2node[a]].rank=b;
	
	temp=index2node[a];
	index2node[a]=index2node[b];
	index2node[b]=temp;
}
//int binsearch(int left,int right,int id){
//	if(left==right){
//		if(cmp(left,id))return left;
//		else return left+1;
//	}
//	int mid=(left+right)/2;
//	if(cmp(mid,id)){
//		return binsearch(left,mid,id);
//	}
//	else{
//		return binsearch(mid+1,right,id);
//	}
//}
int main(){
	freopen("A1129.txt","r",stdin);
	scanf("%d%d",&n,&k);
	fill(G,G+n,-1);
	fill(index2node,index2node+n,-1);
	int temp,p=1;
	scanf("%d",&temp);
	node[0].item=temp;
	node[0].num++;
	node[0].rank=0;
	G[temp]=0;
	index2node[0]=0;
	for(int i=1;i<n;i++){
		scanf("%d",&temp);
		printf("%d:",temp);
		for(int j=0;j<k&&index2node[j]!=-1;j++)printf(" %d",node[index2node[j]].item);
		printf("\n");
		if(G[temp]==-1){
			G[temp]=p;
			index2node[p]=p;
			node[p].item=temp;
			node[p].rank=p;
			p++;
		}
		node[G[temp]].num++;
		int id=node[G[temp]].rank;
//		printf("id=%d\n",id);
//		int ans=0;
//		if(id>0)ans=binsearch(0,id-1,id);
//		for(int j=id;j>=ans+1;j--){
//			Swap(j-1,j);
//		}

		while(cmp(id-1,id)&&id>0){
			Swap(id-1,id);
			id--;
		}
	}
}
