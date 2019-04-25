#include <cstdio>
int main(int argc, char const *argv[])
{
	int a,b,c,n;
	scanf("%d%d%d",&a,&b,&c);
	n=a/b;a=(a-n*b)*10;
	printf("%d.",n);
	for(int i=1;i<=c;i++){
		n=a/b;a=(a-n*b)*10;
		if(i==c&&a/b>=5){
			printf("%d",n+1);
			return 0;
		}
		printf("%d",n);
	}
	return 0;
}