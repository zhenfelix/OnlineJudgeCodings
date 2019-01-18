#include<cstdio>
#include<algorithm>
using namespace std;
const int kmax=10010;
int A[kmax],dp[kmax],k,left[kmax],ans,ans_left,ans_right;
int main(){
	freopen("A1007.txt","r",stdin);
	scanf("%d",&k);
	for(int i=1;i<=k;i++)scanf("%d",&A[i]);
	dp[1]=A[1];left[1]=1;
	for(int i=2;i<=k;i++){
		if(dp[i-1]>=0){
			dp[i]=dp[i-1]+A[i];
			left[i]=left[i-1];
		}
		else{
			dp[i]=A[i];
			left[i]=i;
		}
	}
	ans=-1;
	for(int i=1;i<=k;i++){
		if(dp[i]>ans){
			ans=dp[i];
			ans_left=left[i];
			ans_right=i;
		}
	}
	if(ans<0){
		ans=0;
		ans_left=1;
		ans_right=k;
	}
	printf("%d %d %d",ans,A[ans_left],A[ans_right]);
	return 0;
}

