#include<cstdio>
int main()
{
	int T,i=1;
	long long a,b,c,res;
	bool flag;
	scanf("%d",&T);
	while(T--){
		scanf("%lld%lld%lld",&a,&b,&c);
		res=a+b;
		if(a>0&&b>0&&res<0)flag=true;
		else if(a<0&&b<0&&res>=0)flag=false;
		else if(res>c)flag=true;
		else flag=false;
		if(flag==true)printf("Case #%d: true\n",i++);
		else printf("Case #%d: false\n",i++);
	}
	return 0;
}
