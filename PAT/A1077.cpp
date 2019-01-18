#include<cstdio>
#include<cstring>
void reverse(char *p, int n){
	int i;
	char temp;
	for(i=0;i<n/2;i++){
		temp=p[i];
		p[i]=p[n-1-i];
		p[n-1-i]=temp;
	}
}
int com(char *a,char *b,int n){
	int i;
	for(i=0;i<n;i++)if(a[i]!=b[i])break;
	return i;
}
int main(){
	freopen("A1077.txt","r",stdin);
	int count,N,i=2;
	char a[300]={0},b[300]={0};
	scanf("%d\n",&N);
	gets(a);reverse(a,strlen(a));
	gets(b);reverse(b,strlen(b));
	count=strlen(a)<strlen(b)?strlen(a):strlen(b);
	count=com(a,b,count);
	b[300]={0};
	while(count>0&&i++<N){
		gets(b);reverse(b,strlen(b));
		count=com(a,b,count);
	}
	if(count==0)printf("nai\n");
	else{
		for(i=0;i<count;i++)printf("%c",a[count-1-i]);
		printf("\n");
	}
	return 0;
		
}
