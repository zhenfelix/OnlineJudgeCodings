#include<cstdio>
#include<cstring>
int main()
{
	freopen("B1021.txt","r",stdin);
	int i,count[10]={0},len;
	char a[1010];
	gets(a);
	len=strlen(a);
	for(i=0;i<len;i++)count[a[i]-'0']++;
	for(i=0;i<10;i++)if(count[i]!=0)printf("%d:%d\n",i,count[i]);
	return 0;
}
