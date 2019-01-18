#include<cstdio>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;
struct Node{
	int idx;
	int key;
	int next;
}temp;
map<int,Node>node;
vector<Node>node_new;
bool cmp(Node a,Node b){
	return a.key<b.key;
}
int main(){
	freopen("A1052.txt","r",stdin);
	int n,head,idx;
	scanf("%d%d",&n,&head);
	for(int i=0;i<n;i++){
		scanf("%d%d%d",&temp.idx,&temp.key,&temp.next);
		node[temp.idx]=temp;
	}
	int p=head,count=0;
	while(p!=-1){
		node_new.push_back(node[p]);
		p=node[p].next;
		count++;
		if(node.find(p)==node.end())break;
	}
	sort(node_new.begin(),node_new.begin()+count,cmp);
	if(count>0)printf("%d %05d\n",count,node_new[0].idx);
	else printf("%d -1\n",count);
	for(int i=0;i<count;i++){
		if(i<count-1)printf("%05d %d %05d\n",node_new[i].idx,node_new[i].key,node_new[i+1].idx);
		else printf("%05d %d -1\n",node_new[i].idx,node_new[i].key);
	}
	return 0;
}
