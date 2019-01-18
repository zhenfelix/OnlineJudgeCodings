#include<cstdio>
#include<cmath>
#define A 17
#define B 29

using namespace std;

int sum(int a,int b,int c){
	int r;
	return a*A*B+b*B+c;
}

int main(){
	freopen("B1037.txt","r",stdin);
	int a,b,c,ans,p[3];
	bool neg=false;
	scanf("%d.%d.%d",&a,&b,&c);
	ans=sum(a,b,c);
	scanf("%d.%d.%d",&a,&b,&c);
	ans-=sum(a,b,c);
	ans=-ans;
	if(ans<0)neg=true,ans=-ans;
	p[2]=ans%B;
	ans/=B;
	p[1]=ans%A;
	p[0]=ans/A;
	if(neg)printf("-");
	printf("%d.%d.%d",p[0],p[1],p[2]);
	return 0;
	
}
