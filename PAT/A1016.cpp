#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
struct record{
	char name[25],mark[10];
	int mo,dd,hh,mm;
}entry[1010],left,right;

bool cmp(record a,record b){
	if(strcmp(a.name,b.name)!=0)return strcmp(a.name,b.name)<0;
	else if(a.mo!=b.mo)return a.mo<b.mo;
	else if(a.dd!=b.dd)return a.dd<b.dd;
	else if(a.hh!=b.hh)return a.hh<b.hh;
	else return a.mm<b.mm;
}
void diff(record a,record b,int* rate,int n,int &t,int &cost){
	t=0,cost=0;
	record temp=a;
	while(temp.mm<b.mm||temp.hh<b.hh||temp.dd<b.dd){
		t++;
		cost+=(*(rate+temp.hh));
		temp.mm++;
		if(temp.mm==60)temp.mm=0,temp.hh++;
		if(temp.hh==24)temp.hh=0,temp.dd++;
	}
	
}

int main(){
	freopen("A1016.txt","r",stdin);
	int i,n,rate[24],t;
	char *p;
	int temp=0,cost;
	for(i=0;i<24;i++)scanf("%d",&rate[i]);
	scanf("%d",&n);
	for(i=0;i<n;i++)scanf("%s %d:%d:%d:%d %s\n",entry[i].name,&entry[i].mo,
	&entry[i].dd,&entry[i].hh,&entry[i].mm,entry[i].mark);
	sort(entry,entry+n,cmp);
	bool flag=false,begin=true;
	p=entry[n-1].name;
	for(i=0;i<n;i++){
		if(strcmp(p,entry[i].name)!=0&&begin==true)p=entry[i].name,printf("%s %02d\n",p,entry[i].mo),
			begin=false;
		else if(strcmp(p,entry[i].name)!=0&&begin==false)p=entry[i].name,printf("Total amount: $%.2f\n%s %02d\n",
			temp/100.0,p,entry[i].mo),temp=0;
		if(strcmp(entry[i].mark,"on-line")==0){
			left=entry[i],flag=true;
		}
		else if(strcmp(entry[i].mark,"off-line")==0&&flag==true&&strcmp(p,entry[i].name)==0){
			right=entry[i],flag=false,diff(left,right,rate,24,t,cost);	
			printf("%02d:%02d:%02d %02d:%02d:%02d %d $%.2f\n",left.dd,left.hh,
			left.mm,right.dd,right.hh,right.mm,t,cost/100.0),temp+=cost;
		}
			
			
		
	}
	printf("Total amount: $%.2lf\n",temp/100.0);
//	for(i=0;i<n;i++)printf("%s %02d:%02d:%02d:%02d %s\n",entry[i].name,
//	entry[i].mo,entry[i].dd,entry[i].hh,entry[i].mm,entry[i].mark);
	return 0;
}
