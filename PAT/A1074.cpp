#include<cstdio>
#include<vector>
#include<map>
using namespace std;
int n,k;
struct Node{
	int value;
	int next;
}temp;
map<int,Node> node;
int node_reverse(int head){
	int p=head,pn,pp=-1,tail,tail_before,r=n,count=0;
	
	while(r/k!=0){
		for(int i=0;i<k;i++){
			pn=node[p].next;
			if(i==0)tail=p;
			node[p].next=pp;
			pp=p;
			p=pn;
		}
		
		if(count==0)head=pp;
		else node[tail_before].next=pp;
		node[tail].next=p;
		tail_before=tail;
		count++;
		r-=k;
		if(p==-1)break;
	}
	
	return head;
}
int main(){
	freopen("A1074.txt","r",stdin);
	int head,idx;
	scanf("%d%d%d",&head,&n,&k);
	for(int i=0;i<n;i++){
		scanf("%d%d%d",&idx,&temp.value,&temp.next);
		node[idx]=temp;
	}
	int p=node_reverse(head);
	for(int i=0;i<node.size();i++){
		if(node[p].next==-1){
			printf("%05d% d %d\n",p,node[p].value,node[p].next);
			break;
		}
		else printf("%05d% d %05d\n",p,node[p].value,node[p].next);
		p=node[p].next;
	}
}
