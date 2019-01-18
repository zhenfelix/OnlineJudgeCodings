#include<cstdio>
#include<cmath>

int main(){
	int n,N,res,i,j;
	char sym;
	freopen("B1027.txt","r",stdin);
	scanf("%d %c",&N,&sym);
	n=sqrt((N+1)/2.0);
	res=N-2*n*n+1;
	for(i=0;i<2*n-1;i++){
		for(j=0;j<(n-1-abs(i-n+1));j++)printf(" ");
		for(j=0;j<(abs(i-n+1)*2+1);j++)printf("%c",sym);
		printf("\n");
	}
	printf("%d\n",res);
	return 0;
}
