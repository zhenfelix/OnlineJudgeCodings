#include<cstdio>
#include<algorithm>
using namespace std;
int a[100010],n,p;
int binsrch(int i,long long x){
	int l=i+1,r=n-1,m;
	if(a[n-1]<=x)return n;
	while(l<r){
		m=(l+r)/2;
		if(a[m]>x)r=m;
		else l=m+1;
		
	}
	return r;
}
int main(){
	freopen("B1030.txt","r",stdin);
	int ans=1;
	scanf("%d%d",&n,&p);
	for(int i=0;i<n;i++)scanf("%d",&a[i]);
	sort(a,a+n);
	for(int i=0;i<n;i++){
		ans=max(ans,binsrch(i,p*a[i])-i);
	}
	printf("%d",ans);
	return 0;
}
