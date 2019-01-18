#include<cstdio>
#include<stack>
#include<map>
using namespace std;
struct Node{
	char value;
	int next;
}temp;
map<int,Node>node;
stack<int>a1,a2;
void trans(int x,int choice){
	while(x!=-1){
		if(choice==1)a1.push(x);
		else a2.push(x);
		
		x=node[x].next;
		
	}
}
int main(){
	freopen("A1032.txt","r",stdin);
	int head1,head2,n,p;
	scanf("%d%d%d",&head1,&head2,&n);
	for(int i=0;i<n;i++){
		scanf("%d %c%d",&p,&temp.value,&temp.next);
		node[p]=temp;
	}
	
	trans(head1,1);
	trans(head2,2);
	int temp,count=0;
	
	while(!a1.empty()&&!a2.empty()){
		if(a1.top()==a2.top()){
			temp=a1.top();
			a1.pop();
			a2.pop();
			count++;
		}
		else break;
	}
	if(count==0)printf("-1");
	else printf("%05d",temp);
	return 0;
	
}
