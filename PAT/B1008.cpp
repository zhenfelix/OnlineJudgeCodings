#include<cstdio>
int main()
{
	int a[110];
	int n,m,i,count=0;
	scanf("%d%d",&n,&m);
	for(i=0;i<n;i++)scanf("%d",&a[i]);
	m=m%n;
	for(i=n-m;i<n;i++)
	{
		printf("%d",a[i]);
		if(count<n)printf(" ");
		count++;
	}
	for(i=0;i<n-m;i++)
	{
		printf("%d",a[i]);
		if(count<n-1)printf(" ");
		count++;
	}
}
