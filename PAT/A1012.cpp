#include<cstdio>
#include<algorithm>

using namespace std;

struct student{
	int id;
	int score[4];
}stu[2010];
int now,Rank[10000010][4]={0};

bool cmp(student a,student b){
	return a.score[now]>b.score[now];
}
int main(){
	//printf("ok\n");
	freopen("A1012.txt","r",stdin);
	int n,m,i,temp;
	char course[]={'A','C','M','E'};
	scanf("%d%d",&n,&m);
	for(i=0;i<n;i++){
		scanf("%d%d%d%d",&stu[i].id,&stu[i].score[1],&stu[i].score[2],&stu[i].score[3]);
		stu[i].score[0]=(stu[i].score[1]+stu[i].score[2]+stu[i].score[3])/3.0+0.5;
	}
	for(now=0;now<4;now++){
		sort(stu,stu+n,cmp);
		Rank[stu[0].id][now]=1;
		for(i=1;i<n;i++){
			if(stu[i].score[now]==stu[i-1].score[now])Rank[stu[i].id][now]=Rank[stu[i-1].id][now];
			else Rank[stu[i].id][now]=i+1;
		}
	}
	for(i=0;i<m;i++){
		scanf("%d",&temp);
		if(Rank[temp][0]==0)printf("N/A\n");
		else{
			int k=0;
			for(int j=1;j<4;j++){
				if(Rank[temp][j]<Rank[temp][k])k=j;
			}
			printf("%d %c\n",Rank[temp][k],course[k]);
		}
	}
	return 0;
}
