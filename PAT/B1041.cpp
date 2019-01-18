#include<cstdio>
#define N 1000
struct Info{
	long long number;
	int seat;
}stu[N+1];
int main()
{
	int i,n,m,query,test,seat;
	long long number;
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%lld %d %d",&number,&test,&seat);
		stu[test].number=number;
		stu[test].seat=seat;
	}
	scanf("%d",&m);
	for(i=0;i<m;i++){
		scanf("%d",&query);
		printf("%lld %d\n",stu[query].number,stu[query].seat);
	}
	return 0;
}
