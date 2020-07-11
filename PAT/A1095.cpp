#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<map>
using namespace std;
#define maxn 10010
int n,k,Count=0;
struct car{
	char id[8];
	int time;
	char flag[5];
}all[maxn],valid[maxn];
map<string,int> park;
int TimeConv(int hh,int mm,int ss){
	return hh*3600+mm*60+ss;
}
bool cmpTimeId(car a,car b){
	if(strcmp(a.id,b.id))return strcmp(a.id,b.id)<0;
	else return a.time<b.time;
}
bool cmpTime(car a,car b){
	return a.time<b.time;
}
int main(){
	//freopen("A1095.txt","r",stdin);
	int hh,mm,ss;
	scanf("%d%d",&n,&k);
	for(int i=0;i<n;i++){
		scanf("%s %d:%d:%d %s",all[i].id,&hh,&mm,&ss,all[i].flag);
		all[i].time=TimeConv(hh,mm,ss);
		park[all[i].id]=0;//initialize
	}
	sort(all,all+n,cmpTimeId);
	for(int i=0;i<n-1;){
		if(strcmp(all[i].id,all[i+1].id)==0&&strcmp(all[i].flag,"in")==0
		&&strcmp(all[i+1].flag,"out")==0){
			valid[Count++]=all[i];
			valid[Count++]=all[i+1];
			park[all[i].id]+=all[i+1].time-all[i].time;
			i=i+2;
		}
		else i++;
	}
	sort(valid,valid+Count,cmpTime);
	int num=0,now=0,temp;
	for(int i=0;i<k;i++){
		scanf("%d:%d:%d",&hh,&mm,&ss);
		temp=TimeConv(hh,mm,ss);
		while(valid[now].time<=temp&&now<Count){
			if(strcmp(valid[now].flag,"in")==0)num++;
			else num--;
			now++;
		}
		printf("%d\n",num);
	}
	int maxT=0;
	for(map<string,int>::iterator it=park.begin();it!=park.end();it++){
		if(it->second>maxT)maxT=it->second;
	}
	for(map<string,int>::iterator it=park.begin();it!=park.end();it++){
		if(it->second==maxT)printf("%s ",it->first.c_str());
	}
	printf("%02d:%02d:%02d",maxT/3600,(maxT%3600)/60,(maxT%3600)%60);
}
