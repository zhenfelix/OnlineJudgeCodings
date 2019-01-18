#include<cstdio>
#include<cstring>

int main(){
	freopen("A1005.txt","r",stdin);
	int sum=0,num[10],len,count=0;
	char N[110],mark[][10]={"zero","one","two","three","four","five","six","seven","eight","nine"};
	gets(N);
	len=strlen(N);
	for(int i=0;i<len;i++)sum+=(N[i]-'0');
	do{
		num[count++]=sum%10;
		sum/=10;
	}while(sum!=0);
	for(int i=count-1;i>=0;i--){
		printf("%s",mark[num[i]]);
		if(i!=0)printf(" ");
	}
	return 0;
}
