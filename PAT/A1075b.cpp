#include<cstdio>
#include<algorithm>
using namespace std;
#define maxn 10010
#define maxk 10
int n,k,m,p[maxk];
struct user{
	int id,num=0,total=0,rank;
	int score[maxk];
	bool flag=false;
}stu[maxn];
bool cmp(user a,user b){
	if(a.flag!=b.flag)return a.flag;
	else if(a.total!=b.total)return a.total>b.total;
	else if(a.num!=b.num)return a.num>b.num;
	else return a.id<b.id;
}
void init(){
	for(int i=1;i<=n;i++){
		for(int j=1;j<=k;j++)stu[i].score[j]=-1;
	}
}
int main(){
	freopen("A1075.txt","r",stdin);
	scanf("%d%d%d",&n,&k,&m);
	init();
	for(int i=1;i<=k;i++)scanf("%d",&p[i]);
	for(int i=1;i<=m;i++){
		int idx,pid,temp;
		scanf("%d%d%d",&idx,&pid,&temp);
		if(temp==-1)temp=0;
		else stu[idx].flag=true;
		if(temp>stu[idx].score[pid]){
			stu[idx].score[pid]=temp;
			stu[idx].id=idx;
			if(temp==p[pid])stu[idx].num++;
		}
	}
	for(int i=1;i<=n;i++){
		int sum=0;
		for(int j=1;j<=k;j++){
			if(stu[i].score[j]>0)sum+=stu[i].score[j];
		}
		stu[i].total=sum;
	}
	sort(stu+1,stu+n+1,cmp);
	stu[1].rank=1;
	for(int i=2;i<=n;i++){
		if(stu[i].total==stu[i-1].total)stu[i].rank=stu[i-1].rank;
		else stu[i].rank=i;
	}
	int i=1;
	while(stu[i].flag){
		printf("%d %05d %d",stu[i].rank,stu[i].id,stu[i].total);
		for(int j=1;j<=k;j++){
			if(stu[i].score[j]==-1)printf(" -");
			else printf(" %d",stu[i].score[j]);
		}
		printf("\n");
		i++;
	}
	return 0;
}
