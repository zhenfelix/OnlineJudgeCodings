#include<cstdio>
int main()
{
	int ay,ah,by,bh,a=0,b=0,n,p;
	scanf("%d",&n);
	while(n--)
	{
		scanf("%d%d%d%d",&ay,&ah,&by,&bh);
		p=ay+by;
		if((p==ah)&&(p!=bh))b++;
		else if ((p!=ah)&&(p==bh))a++;
	}
	printf("%d %d",a,b);
	return 0;
}
