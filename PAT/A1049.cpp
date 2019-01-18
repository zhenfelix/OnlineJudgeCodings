#include<cstdio>
int main(){
	freopen("A1049.txt","r",stdin);
	int n,left,right,now,a=1,ans=0;
	scanf("%d",&n);
	while(n/a!=0){
		left=n/(a*10);
		right=n%a;
		now=n/a%10;
		if(now==0)ans+=left*a;
		else if(now==1)ans+=left*a+right+1;
		else ans+=left*a+a;
		a*=10;
	}
	printf("%d",ans);
	return 0;
}
