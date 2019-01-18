#include<cstdio>
#include<cstring>
int main(){
    freopen("A1001.txt","r",stdin);
	long long a,b,r;
	int i,n=0,str[10];
	scanf("%lld%lld",&a,&b);
	r=a+b;
	if(r<0)printf("-"),r=-r;
	do{
		str[n++]=r%10;
		r=r/10;
	}while(r!=0);
	for(i=1;i<=n;i++){
		printf("%d",str[n-i]);
		if((n-i)%3==0&&i!=n)printf(",");
	}
	return 0;
}
