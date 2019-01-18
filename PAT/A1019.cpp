#include<cstdio>
int main(){
	freopen("A1019.txt","r",stdin);
	int N,n=0,i,b,a[40];
	bool flag=true;
	scanf("%d%d",&N,&b);
	do{
		a[n++]=N%b;
		N/=b;
	}while(N!=0);
	i=0;
	while((flag==true)&&(i<=n/2)){
		if(a[i]!=a[n-1-i])flag=false;
		i++;
	}
	if(flag==true)printf("Yes\n");
	else printf("No\n");
	for(i=n-1;i>=0;i--){
		printf("%d",a[i]);
		if(i!=0)printf(" ");
	}
	return 0;
}
