#include<cstdio>
#include<cstring>

int main()
{
	//freopen("A1031.txt","r",stdin);
	char str[100];
	int i,j,n1,n2,N;
	gets(str);
	N=strlen(str);
	//printf("%d\n",N);
	n1=(N+2)/3,n2=(N+2)-2*n1;
	for(i=0;i<n1-1;i++){
		printf("%c",str[i]);
		for(j=0;j<n2-2;j++)printf(" ");
		printf("%c\n",str[N-1-i]);
	}
	for(j=0;j<n2;j++)printf("%c",str[n1-1+j]);
	return 0;
}
