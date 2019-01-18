#include<cstdio>
int main()
{
	freopen("A1011.txt", "r", stdin);
	char mark[3]={'W','T','L'};
	float p=1,mx,score;
	int i,idx=0,j;
	for(i=0;i<3;i++){
		mx=0;
		for(j=0;j<3;j++){
			scanf("%f",&score);
			if(score>mx)mx=score,idx=j;
		}
		p*=mx;
		printf("%c ",mark[idx]);
	}
	p=(p*0.65-1)*2;
	printf("%.2f",p);
	return 0;
}
