#include<cstdio>
#include<algorithm>
using namespace std;
const int nmax=10010;
const int mmax=110;
int dp[nmax][mmax]={0},w[nmax],n,m;
bool choice[nmax][mmax]={false},flag[nmax]={false};
bool cmp(int a,int b){
	return a>b;
}
int main(){
	freopen("A1068.txt","r",stdin);
	scanf("%d%d",&n,&m);
	for(int i=1;i<=n;i++)scanf("%d",&w[i]);
	sort(w+1,w+1+n,cmp);
	for(int i=1;i<=n;i++){
		for(int v=w[i];v<=m;v++){
				if(dp[i-1][v-w[i]]+w[i]<dp[i-1][v]){
					dp[i][v]=dp[i-1][v];
				}
				else{
					dp[i][v]=dp[i-1][v-w[i]]+w[i];
					choice[i][v]=true;
				}
		}
	}
	if(dp[n][m]!=m)printf("No Solution\n");
	else{
		int i=n,v=m;
		while(i>=1){
			if(choice[i][v]){
				flag[i]=true;
				v=v-w[i];
			}
			i--;
		}
		int num=0;
		for(int i=n;i>=1;i--){
			if(flag[i]){
				if(num!=0)printf(" ");
				printf("%d",w[i]);
				num++;
			}
		}
	}
	return 0;
}
