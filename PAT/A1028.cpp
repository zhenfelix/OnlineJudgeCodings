#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int now;
struct record{
	int id,score;
	char name[10];
}stu[100010];
bool cmp(record a,record b){
	if(now==1)return a.id<b.id;
	else if(now==2){
		if(strcmp(a.name,b.name)!=0)return strcmp(a.name,b.name)<0;
		else return a.id<b.id;
	}
	else if(now==3){
		if(a.score!=b.score)return a.score<b.score;
		else return a.id<b.id;
	}
}
int main(){
	freopen("A1028.txt","r",stdin);
	int n,i;
	scanf("%d%d",&n,&now);
	for(i=0;i<n;i++)scanf("%d %s %d",&stu[i].id,stu[i].name,&stu[i].score);
	sort(stu,stu+n,cmp);
	for(i=0;i<n;i++)printf("%06d %s %d\n",stu[i].id,stu[i].name,stu[i].score);
	return 0;
}
