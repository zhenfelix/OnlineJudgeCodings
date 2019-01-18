#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int now;
struct record{
	char id[15];
	int score,loc,rank_l,rank_g;
}stu[30010];
bool cmp(record a,record b){
	if(now==0)return a.score>b.score;
	else if(now==1){
		if(a.loc!=b.loc)return a.loc<b.loc;
		else if(a.score!=b.score)return a.score>b.score;
	}
	else if(now==2){
		if(a.rank_g!=b.rank_g)return a.rank_g<b.rank_g;
		else if(strcmp(a.id,b.id)!=0)return strcmp(a.id,b.id)<0;
	}
}
int main(){
	freopen("A1025.txt","r",stdin);
	int i,j,n,m,count=0;
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d",&m);
		for(j=0;j<m;j++){
			scanf("%s %d",stu[count].id,&stu[count].score);
			stu[count].loc=i+1;
			count++;
		}
	}
	now=0;
	sort(stu,stu+count,cmp);
	stu[0].rank_g=1;
	for(i=1;i<count;i++){
		if(stu[i].score==stu[i-1].score)stu[i].rank_g=stu[i-1].rank_g;
		else stu[i].rank_g=i+1;
	}
	now=1;
	sort(stu,stu+count,cmp);
	int num,temp;
	temp=stu[count].loc;
	for(i=0;i<count;i++){
		if(temp!=stu[i].loc)num=1,stu[i].rank_l=1,temp=stu[i].loc;
		else{
			if(stu[i].score==stu[i-1].score)stu[i].rank_l=stu[i-1].rank_l;
	    	else stu[i].rank_l=num+1;
	    	num++;
	    	//printf("ok\n");
		}
		
	}
	now=2;
	sort(stu,stu+count,cmp);
	printf("%d\n",count);
	for(i=0;i<count;i++){
		printf("%s %d %d %d\n",stu[i].id,stu[i].rank_g,stu[i].loc,stu[i].rank_l);
	}
	return 0;
}
