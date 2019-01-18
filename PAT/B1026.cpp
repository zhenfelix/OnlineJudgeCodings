#include<cstdio>
int main()
{
	int c1,c2,t,r,T=100;
	scanf("%d%d",&c1,&c2);
	r=(c2-c1)%100;
	t=(c2-c1)/100;
	if(r>=50)t++;
	printf("%02d:%02d:%02d\n",t/3600,t%3600/60,t%60);
}
