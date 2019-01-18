#include<cstdio>
#include<cstring>
using namespace std;
char a[1010],q[1010];
int main(){
	freopen("B1017.txt","r",stdin);
	int x,temp=0,b,r=0,len;
	scanf("%s %d",a,&b);
	len=strlen(a);
	for(int i=0;i<len;i++){
		x=a[i]-'0';
		temp=r*10+x;
		r=temp%b;
		q[i]='0'+temp/b;
	}
	for(int i=0;i<len;i++){
		
		if(i==0&&q[i]=='0'&&len>1);
		else printf("%c",q[i]);
	}
	printf(" %d",r);
	return 0;
}
