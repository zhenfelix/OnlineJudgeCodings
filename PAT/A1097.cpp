#include<cstdio>
#include<cmath>
using namespace std;
struct Node{
	int key;
	int next;
}node[100005];
bool HashTable[10005]={0};
void show(int head){
	int p=head;
	while(p!=-1){
		if(node[p].next!=-1)printf("%05d %d %05d\n",p,node[p].key,node[p].next);
		else printf("%05d %d -1\n",p,node[p].key);
		p=node[p].next;
	}
}
int main(){
	freopen("A1097.txt","r",stdin);
	int head,idx,n,temp,head2;
	scanf("%d%d",&head,&n);
	for(int i=0;i<n;i++){
		scanf("%d",&idx);
		scanf("%d%d",&node[idx].key,&node[idx].next);
	}
	int p=head,pn=node[head].next,count=0,p2;
	while(pn!=-1){
		temp=node[pn].key;
		temp=abs(temp);
		if(HashTable[temp]){
			
			node[p].next=node[pn].next;
			if(count==0)head2=pn,p2=head2;
			else{
				node[p2].next=pn;
				p2=pn;
			}
			pn=node[p].next;
			count++;
		}
		else{
			HashTable[temp]=true;
		    p=node[p].next;
		    pn=node[p].next;
		} 
	}
	node[p2].next=-1;
	show(head);
	show(head2);
	return 0;
}
