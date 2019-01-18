#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

struct student{
	int de,cai,sum,flag;
	char id[10];
}stu[100010];
bool high(student a,student b){
	if(a.flag!=b.flag)return a.flag<b.flag;
	else if(a.sum!=b.sum)return a.sum>b.sum;
	else if(a.de!=b.de)return a.de>b.de;
	else return strcmp(a.id,b.id)<0;
}
int main(){
	freopen("B1035.txt","r",stdin);
	int n,l,h,i,m;
	scanf("%d%d%d",&n,&l,&h);
	m=n;
	for(i=0;i<n;i++){
		scanf("%s%d%d",stu[i].id,&stu[i].de,&stu[i].cai);
		stu[i].sum=stu[i].de+stu[i].cai;
		if(stu[i].de<l||stu[i].cai<l)stu[i].flag=5,m--;
		else if(stu[i].de>=h&&stu[i].cai>=h)stu[i].flag=1;
		else if(stu[i].de>=h&&stu[i].cai<h)stu[i].flag=2;
		else if(stu[i].cai<=stu[i].de)stu[i].flag=3;
		else stu[i].flag=4;
	}
	sort(stu,stu+n,high);
	printf("%d\n",m);
	for(i=0;i<m;i++)printf("%s %d %d\n",stu[i].id,stu[i].de,stu[i].cai);
	return 0;
}
