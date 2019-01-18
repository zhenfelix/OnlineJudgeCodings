#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
struct user{
	int id=0,sum=0,s[6]={-1,-1,-1,-1,-1,-1},count=0,rank;
	bool flag=false;
}stu[10010],stu_v[10010];
bool cmp(user a,user b){
	if(a.sum!=b.sum)return a.sum>b.sum;
	else if(a.count!=b.count)return a.count>b.count;
	else return a.id<b.id;
}
int main(){
	freopen("A1075.txt","r",stdin);
	int n,k,m,i,j,p[6],temp,score,ID,num=0,u[1010];
	scanf("%d%d%d",&n,&k,&m);
	for(i=1;i<=k;i++)scanf("%d",&p[i]);
	for(i=0;i<m;i++){
		scanf("%d%d%d",&ID,&temp,&score);
		if(stu[ID].id==0)u[num++]=ID,stu[ID].id=ID;
		if(score==-1)stu[ID].s[temp]=0;
		else if(score>=stu[ID].s[temp])stu[ID].s[temp]=score,stu[ID].flag=true;
		if(score==p[temp])stu[ID].count++;

		
	}
	for(i=0;i<num;i++){
		stu_v[i]=stu[u[i]];
		for(j=1;j<=k;j++){
			if(stu_v[i].s[j]!=-1)stu_v[i].sum+=stu_v[i].s[j];
		}
	}
	sort(stu_v,stu_v+num,cmp);
	stu_v[0].rank=1;
	for(i=1;i<num;i++){
		if(stu_v[i].sum==stu_v[i-1].sum)stu_v[i].rank=stu_v[i-1].rank;
		else stu_v[i].rank=i+1;
	}
	for(i=0;i<num;i++){
		if(stu_v[i].flag==true){
			printf("%d %05d %d",stu_v[i].rank,stu_v[i].id,stu_v[i].sum);
    		for(j=1;j<=k;j++){
	    		if(stu_v[i].s[j]!=-1)printf(" %d",stu_v[i].s[j]);
		    	else printf(" -");
		    }
    		printf("\n");
		}
		
	}
	return 0;

}
