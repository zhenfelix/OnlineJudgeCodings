#include<cstdio>
#include<cstring>
int main(){
	freopen("B1002.txt","r",stdin);
	char a[100],mark[][7]={"ling","yi","er","san","si","wu","liu","qi","ba","jiu"};
	int s=0,i,len,temp[10],count=0;
	gets(a);
	len=strlen(a);
	for(i=0;i<len;i++)s+=(a[i]-'0');
	do{
		temp[count++]=s%10;
		s/=10;
	}while(s!=0);
	for(i=count-1;i>=0;i--){
		printf("%s",mark[temp[i]]);
		if(i!=0)printf(" ");
	}
	return 0;
}
