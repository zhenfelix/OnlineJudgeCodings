#include<cstdio>
typedef long long LL;
LL q[1000010];
int n1,n2;
int main(){
	freopen("A1029.txt","r",stdin);
	int count=0;
	LL temp,ans=0;
	scanf("%d",&n1);
	for(int i=0;i<n1;i++)scanf("%lld",&q[i]);
	scanf("%d",&n2);
	int j=0,mid=(n1+n2+1)/2;
	for(int i=0;i<n2;i++){
		scanf("%lld",&temp);
		while(q[j]<temp&&j<n1){
			count++;
			if(count==mid){
				ans=q[j];
				break;
			}
			j++;
		}
		if(ans!=0)break;
		count++;
		if(count==mid){
			ans=temp;
			break;
		}
	}
	printf("%d",ans);
	return 0;
}
