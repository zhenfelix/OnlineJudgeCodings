#include<cstdio>
#include<cmath>
int main()
{
	int n,m,i,j;
	char sym;
	//freopen("B1036.txt","r",stdin);
	scanf("%d %c",&n,&sym);
	//if(n%2==1)m=n/2+1;
	//else m=n/2;
	m=round(n/2);
	m=(int) m;
	for(i=0;i<n;i++)printf("%c",sym);
	printf("\n");
	for(j=0;j<m-2;j++){
		printf("%c",sym);
		for(i=0;i<n-2;i++)printf(" ");
		printf("%c\n",sym);
	}
	for(i=0;i<n;i++)printf("%c",sym);
	return 0;
}
