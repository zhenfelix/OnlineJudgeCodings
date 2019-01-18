#include<cstdio>
#include<cmath>
#define A 17
#define B 29

using namespace std;

long long sum(int a,int b,int c){
	return a*A*B+b*B+c;
}

int main(){
	freopen("A1058.txt","r",stdin);
	int a,b,c,p[3];
	long long ans;
	bool neg=false;
	scanf("%d.%d.%d",&a,&b,&c);
	ans=sum(a,b,c);
	scanf("%d.%d.%d",&a,&b,&c);
	ans+=sum(a,b,c);
	if(ans<0)neg=true,ans=-ans;
	p[2]=ans%B;
	ans/=B;
	p[1]=ans%A;
	p[0]=ans/A;
	if(neg)printf("-");
	printf("%d.%d.%d",p[0],p[1],p[2]);
	return 0;
	
}
