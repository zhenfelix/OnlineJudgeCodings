#include<cstdio>
#include<algorithm>
using namespace std;
#define maxn 100010
int main(){
	freopen("A1046.txt","r",stdin);
	int n,m,total,a[maxn],sum[maxn];
	scanf("%d",&n);
	for(int i=1;i<=n;i++)scanf("%d",&a[i]);
	sum[1]=0;
	for(int i=2;i<=n;i++)sum[i]=sum[i-1]+a[i-1];
	total=sum[n]+a[n];
	scanf("%d",&m);
	for(int i=0;i<m;i++){
		int a,b,temp;
		scanf("%d%d",&a,&b);
		if(a>b)swap(a,b);
		temp=sum[b]-sum[a];
		temp=min(total-temp,temp);
		printf("%d\n",temp);
	}
	return 0;
}
