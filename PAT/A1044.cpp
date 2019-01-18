#include<cstdio>
int sum[100010];
int upper_bound(int l,int r,int x){
	int mid;
	while(r>l){
		mid=(l+r)/2;
		if(sum[mid]>x)r=mid;
		else l=mid+1;
	}
	return r;
}
int main(){
	freopen("A1044.txt","r",stdin);
	int n,m,NoLessM=100000010;
	scanf("%d%d",&n,&m);
	sum[0]=0;
	for(int i=1;i<=n;i++)scanf("%d",&sum[i]),sum[i]+=sum[i-1];
	for(int i=0;i<=n;i++){
		int j=upper_bound(i,n+1,m+sum[i]);
		if(sum[j-1]-sum[i]==m){
			NoLessM=m;
			break;
		}
		else if(j<=n&&sum[j]-sum[i]<NoLessM)NoLessM=sum[j]-sum[i];
	}
	for(int i=0;i<=n;i++){
		int j=upper_bound(i,n+1,m+sum[i]);
		if(sum[j-1]-sum[i]==NoLessM)printf("%d-%d\n",i+1,j-1);
		else if(sum[j]-sum[i]==NoLessM)printf("%d-%d\n",i+1,j);
	}
	return 0;
}
