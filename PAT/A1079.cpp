#include<cstdio>
#include<vector>
#include<queue>
#include<map>
#include<cmath>
using namespace std;
struct Node{
	int level;
	vector<int>child;
}node[100010];
map<int,int>num;
int n;
double p,r,sum=0.0;
void bfs(){
	queue<Node>q;
	node[0].level=0;
	q.push(node[0]);
	while(!q.empty()){
		Node temp=q.front();
		q.pop();
		//printf("temp node= level=%d\n",temp.level);
		for(int i=0;i<temp.child.size();i++){
			node[temp.child[i]].level=temp.level+1;
			q.push(node[temp.child[i]]);
			//printf("node=%d level=%d; ",temp.child[i],node[temp.child[i]].level);
		}
		//printf("\n");
	}
}
int main(){
	freopen("A1079.txt","r",stdin);
	int temp,v;
	scanf("%d%lf%lf",&n,&p,&r);
	for(int i=0;i<n;i++){
		scanf("%d",&temp);
		if(temp==0){
			scanf("%d",&v);
			num[i]=v;
		}
		else{
			for(int j=0;j<temp;j++){
				scanf("%d",&v);
				node[i].child.push_back(v);
			}
		}
	}
	bfs();
	for(map<int,int>::iterator it=num.begin();it!=num.end();it++)sum+=pow(1+r/100.0,(double) node[it->first].level)*(it->second)*p;
	//sum=((int) (sum*100))%10>=5?sum+0.1:sum;
	printf("%.1f",sum);
	return 0;
}
