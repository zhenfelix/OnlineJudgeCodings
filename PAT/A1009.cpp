#include<cstdio>
#define Amax 1001
#define Bmax 2001
struct Poly{
	int exp;
	double coef;
}a[Amax];
int main()
{
	double ans[Bmax]={},coef;
	int n,m,i,j,exp,count=0;
	scanf("%d",&n);
	for(i=0;i<n;i++)scanf("%d %lf",&a[i].exp,&a[i].coef);
	scanf("%d",&m);
	for(i=0;i<m;i++){
		scanf("%d %lf",&exp,&coef);
		for(j=0;j<n;j++)ans[exp+a[j].exp]+=coef*a[j].coef;
	}
	for(i=0;i<Bmax;i++){
		if(ans[i]!=0.0)count++;
	}
	printf("%d",count);
	for(i=Bmax-1;i>=0;i--){
		if(ans[i]!=0.0)printf(" %d %.1f",i,ans[i]);
	}
	return 0;
}
