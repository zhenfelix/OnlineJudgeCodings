#include<cstdio>
#define max_k 1001
int main()
{
	double p[max_k]={0},x;
	int k,i,a,count=0;
	scanf("%d",&k);
	for(i=0;i<k;i++){
		scanf("%d%lf",&a,&x);
		p[a]+=x;
	}
	scanf("%d",&k);
	for(i=0;i<k;i++){
		scanf("%d%lf",&a,&x);
		p[a]+=x;
	}
	for(i=0;i<max_k;i++){
		if(p[i]!=0)count++;
	}
	printf("%d",count);
	for(i=max_k-1;i>=0;i--){
		if(p[i]!=0)printf(" %d %.1f",i,p[i]);
	}
	return 0;
}
