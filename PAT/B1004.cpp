#include<cstdio>
struct Info{
	char name[11];
	char id[11];
	int score;
}temp,ans_max,ans_min;
int main()
{
	int n,i;
	scanf("%d",&n);
	ans_max.score=-1;
	ans_min.score=101;
	for(i=0;i<n;i++){
		scanf("%s%s%d",&temp.name,&temp.id,&temp.score);
		if(temp.score>ans_max.score)ans_max=temp;
		if(temp.score<ans_min.score)ans_min=temp;
	}
	printf("%s %s\n",ans_max.name,ans_max.id);
	printf("%s %s\n",ans_min.name,ans_min.id);
	return 0;
}
