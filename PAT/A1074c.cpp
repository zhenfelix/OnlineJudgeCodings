#include<cstdio>
#define maxn 100010
int n,k;
struct Node{
	int data,next;
}node[maxn];
int reverse(int head){
	if(node[head].next==-1)return head;
	int p=node[head].next,h,t;
	h=reverse(p);t=h;
	while(node[t].next!=-1)t=node[t].next;
	node[t].next=head;
	node[head].next=-1;
	return h;
}
int main(){
	freopen("A1074.txt","r",stdin);
	int head;
	scanf("%d%d%d",&head,&n,&k);
	while(n--){
		int temp;
		scanf("%d",&temp);
		scanf("%d%d",&node[temp].data,&node[temp].next);
	}
	int p=head,h=-1,t=-1;
	while(p!=-1){
		p=node[p].next;
		n++;
	}
	n++;
	h=head;
	while(n>=k){
		p=h;
		for(int i=1;i<k;i++){
			p=node[p].next;
		}
		h=node[p].next;
		node[p].next=-1;
		if(t==-1){
			head=reverse(head);
			p=head;
		}
		else{
			node[t].next=reverse(node[t].next);
	    	p=node[t].next;
		}
		while(node[p].next!=-1)p=node[p].next;
		t=p;
		node[t].next=h;
		n=n-k;
	}
	while(head!=-1){
		printf("%05d %d ",head,node[head].data);
		if(node[head].next==-1)printf("-1");
		else printf("%05d\n",node[head].next);
		head=node[head].next;
	}
	return 0;
}
