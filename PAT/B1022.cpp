#include<cstdio>

int format(int x,int d, int *p){
	int count=0;
	do{
		*(p++)=x%d;
		x=x/d;
		count++;
	}while(x!=0);
	return count;
}

int main()
{
	freopen("B1022.txt","r",stdin);
	int a,b,d,count,p[32],i;
	scanf("%d%d%d",&a,&b,&d);
	count=format(a+b,d,p);
	for(i=count-1;i>=0;i--)printf("%d",p[i]);
	return 0;
}
