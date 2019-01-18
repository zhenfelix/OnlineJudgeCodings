#include<cstdio>
#include<cstring>
using namespace std;
const int nmax=1010;
int dp[nmax][nmax]={0};
int main(){
	//freopen("A1040.txt","r",stdin);
	char str[nmax];
	int n,L,ans=1;
	gets(str);
	n=strlen(str);
	for(int i=0;i<n;i++)dp[i][i]=1;
	for(int i=0;i<n-1;i++){
		if(str[i]==str[i+1]){
			dp[i][i+1]=1;
			ans=2;
		}
	}
	for(int L=3;L<=n;L++){
		for(int i=0;i+L-1<n;i++){
			int j=i+L-1;
			if(str[i]==str[j]&&dp[i+1][j-1]){
				dp[i][j]=1;
				ans=L;
			}
		}
	}
	printf("%d",ans);
	return 0;
}
