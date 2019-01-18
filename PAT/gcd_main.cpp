#include<cstdio>
int gcd(int x,int y){
	return y?gcd(y,x%y):x;
}
int main(){
	freopen("gcd.txt","r",stdin);
	int ans,x,y;
	scanf("%d%d",&x,&y);
	ans=gcd(x,y);
	printf("%d",ans);
	return 0;
}
