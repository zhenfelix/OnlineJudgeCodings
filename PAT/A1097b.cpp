#include<cstdio>
#include<algorithm>
using namespace std;
#define maxn 1000010
struct Node{
	int data;
	int next=-2;
}node[maxn];
bool Hashtable[10010]={false};
bool visit[maxn]={false};
void show(int head){
	while(head!=-1){
		printf("%05d %d ",head,node[head].data);
		if(node[head].next==-1)printf("%d\n",node[head].next);
		else printf("%05d\n",node[head].next);
		head=node[head].next;
	}
}
int main(){
	freopen("A1097.txt","r",stdin);
	int head,n,idx;
	scanf("%d%d",&head,&n);
	for(int i=0;i<n;i++){
		scanf("%d",&idx);
		scanf("%d%d",&node[idx].data,&node[idx].next);
	}
	int p=node[head].next,head2=-1,pre=head;
	visit[head]=true;
	while(p!=-1){
		if(node[p].next==-2||visit[p]){
			node[pre].next=-1;
			break;
		}
		visit[p]=true;
		int temp=node[p].data;
		temp=abs(temp);
		if(Hashtable[temp]){
			node[pre].next=node[p].next;
			if(head2==-1)head2=p;
			else{
				int px=head2;
				while(node[px].next!=-1)px=node[px].next;
				node[px].next=p;
			}
			node[p].next=-1;
			p=node[pre].next;
		}
		else{
			Hashtable[temp]=true;
			pre=p;
			p=node[p].next;
		}
	}
	show(head);
	show(head2);
	return 0;
}
