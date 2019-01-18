#include<cstdio>
#include<cstring>
using namespace std;
char str[100010];
int p[100010],t[100010];
int main(){
	freopen("A1093.txt","r",stdin);
	int len,count=0,left=0,right=0,n;
	long long sum=0;
	gets(str);
	len=strlen(str);
	for(int i=0;i<len;i++){
		if(str[i]=='A')p[count++]=left;
		else if(str[i]=='P')left++;
	}
	n=count;
	for(int i=len-1;i>=0;i--){
		if(str[i]=='A')t[--count]=right;
		else if(str[i]=='T')right++;
	}
	for(int i=0;i<n;i++)sum+=(p[i]*t[i]);
	printf("%lld",sum%1000000007);
	return 0;
}
