#include<cstdio>
#define MAX 100001
int main()
{
	int n,i,idx,sco,score[MAX]={},high=-1,mark;
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d%d",&idx,&sco);
		score[idx]+=sco;
		if(score[idx]>high)mark=idx,high=score[idx];
	}
	//for(i=1;i<=n;i++)if(score[i]>high)mark=i,high=score[i];
	printf("%d %d",mark,score[mark]);
	return 0;
}
