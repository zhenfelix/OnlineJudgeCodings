#include<cstdio>
const int nmax=210;
const int lmax=10010;
int fav[nmax],a[lmax],n,m,l,dp[lmax]={0};
void init(){
	for(int i=1;i<=n;i++)fav[i]=-1;
	return;
}
int main(){
	freopen("A1045.txt","r",stdin);
	int temp;
	scanf("%d%d",&n,&m);
	init();
	for(int i=1;i<=m;i++){
		scanf("%d",&temp);
		fav[temp]=i;
	}
	scanf("%d",&l);
	for(int i=1;i<=l;i++){
		scanf("%d",&a[i]);
	}
	for(int i=1;i<=l;i++){
		if(fav[a[i]]!=-1){
			dp[i]=1;//the first one in the subsequence will be ignored
			//single digit always has a length of one
			for(int j=i-1;j>=1;j--){
				if(fav[a[j]]!=-1){
					if(fav[a[j]]<=fav[a[i]]){//the first one in the subsequence will be ignored
					if(dp[j]+1>dp[i])dp[i]=dp[j]+1;
				}
				}
				
			}
		}
	}
	int ans=0;
	for(int i=1;i<=l;i++){
		if(dp[i]>ans)ans=dp[i];
	}
	printf("%d",ans);//the first one in the subsequence will be ignored
	return 0;
}
