#include<cstdio>
#define N 54
int main()
{
	int a[N+1],b[N+1],p[N+1],K,i,j;
	char mp[5]={'S','H','C','D','J'};
	scanf("%d",&K);
	for(i=1;i<=N;i++)scanf("%d",&p[i]),a[i]=i;
	for(j=0;j<K;j++){
		for(i=1;i<=N;i++){
			b[p[i]]=a[i];
		}
		for(i=1;i<=N;i++)a[i]=b[i];
	}
	for(i=1;i<=N;i++){
		b[i]--;
		printf("%c%d",mp[b[i]/13],b[i]%13+1);
		if(i<N)printf(" ");
	}
	return 0;
}
