#include<stdio.h>
int main()
{
	freopen("A1011.txt", "r", stdin);
	char mark[3]={'W','T','L'};
	double score;
	int i,idx=0,j;
	for(i=0;i<3;i++){
		for(j=0;j<3;j++){
			scanf("%lf",&score);
			printf("%.2f ",score);
		}
	}
	return 0;
}
