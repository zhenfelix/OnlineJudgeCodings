#include<cstdio>
#include<algorithm>
#include<cstring>
#include<string>
#include<map>
using namespace std;
#define maxn 1010
struct record{
	char name[25];
	int mo,dd,hh,mm;
	bool flag;
}all[maxn],valid[maxn];
int toll[24],n;
double total;
map<string,int>Count;
bool cmp(record a,record b){
	if(strcmp(a.name,b.name)!=0)return strcmp(a.name,b.name)<0;
	else if(a.mo!=b.mo)return a.mo<b.mo;
	else if(a.dd!=b.dd)return a.dd<b.dd;
	else if(a.hh!=b.hh)return a.hh<b.hh;
	else return a.mm<b.mm;
}
void compute(record a,record b){
	int time=0,dt,ht,mt;
	double money=0;
	dt=a.dd,ht=a.hh,mt=a.mm;
	while(dt<b.dd||ht<b.hh||mt<b.mm){
		time++;
		mt++;
		money+=toll[ht]/100.0;
		if(mt==60)mt=0,ht++;
		if(ht==24)ht=0,dt++;
	}
	printf("%02d:%02d:%02d %02d:%02d:%02d %d $%.2f\n",a.dd,a.hh,a.mm,b.dd,b.hh,b.mm,time,money);
	total+=money;
}
int main(){
	freopen("A1016.txt","r",stdin);
	for(int i=0;i<24;i++)scanf("%d",&toll[i]);
	scanf("%d",&n);
	
	for(int i=0;i<n;i++){
		scanf("%s %d:%d:%d:%d",all[i].name,&all[i].mo,&all[i].dd,&all[i].hh,&all[i].mm);
		char temp[10];
		scanf("%s",temp);
		if(strcmp(temp,"on-line")==0)all[i].flag=true;
		else all[i].flag=false;
	}
	sort(all,all+n,cmp);
	int num=0;
	for(int i=0;i<n-1;i++){
		if(strcmp(all[i].name,all[i+1].name)==0&&all[i].flag&&!all[i+1].flag){
			valid[num++]=all[i];
			valid[num++]=all[i+1];
			if(Count.find(all[i].name)==Count.end())Count[all[i].name]=1;
			else Count[all[i].name]++;
		}
	}
	for(int i=0;i<num;){
		printf("%s %02d\n",valid[i].name,valid[i].mo);
		total=0;
		int temp=Count[valid[i].name];
		for(int k=0;k<temp;k++){
			compute(valid[i],valid[i+1]);
			i=i+2;
		}
		printf("Total amount: $%.2f\n",total);
	}
//	for(int i=0;i<num;i++)printf("%s %02d:%02d:%02d:%02d\n",valid[i].name,valid[i].mo,
//	valid[i].dd,valid[i].hh,valid[i].mm);
	return 0;
}
