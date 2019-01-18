#include<cstdio>
#include<queue>
#include<vector>
using namespace std;
struct mouse{
	int w;
	int rank;
}mp;
vector<mouse> m;
queue<int> q;
void init(){
	while(!q.empty())q.pop();
	m.clear();
}
int main(){
	freopen("A1056.txt","r",stdin);
	init();
	int np,ng,num,group,temp;
	scanf("%d%d",&np,&ng);
	for(int i=0;i<np;i++){
		scanf("%d",&temp);
		mp.w=temp;
		m.push_back(mp);
	}
	for(int i=0;i<np;i++){
		scanf("%d",&temp);
		q.push(temp);
	}
	do{
		num=q.size();
		
		if(num%ng==0)group=num/ng;
		else group=num/ng+1;
		for(int i=0;i<group;i++){
			int k=q.front();
			for(int j=0;j<ng;j++){
				if(i*ng+j+1>num)break;
				if(m[q.front()].w>m[k].w)k=q.front();
				m[q.front()].rank=group+1;
				q.pop();
			}
			q.push(k);
		}
		
	}while(q.size()!=1);
	m[q.front()].rank=1;
	for(int i=0;i<np;i++){
		printf("%d",m[i].rank);
		if(i<np-1)printf(" ");
	}
	return 0;
}
