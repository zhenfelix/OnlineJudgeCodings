#include<cstdio>
#include<cmath>
using namespace std;
#define maxn 410
int n,k,p;
int s[maxn]={0};
int temp[maxn];
bool flag=false;
int int_power(int x,int y){
	int ans=1;
	while(y--)ans*=x;
	return ans;
}

bool cmp(int *a,int *b){
	int sum_a=0,sum_b=0;
	for(int i=0;i<k;i++){
		sum_a+=a[i];
		sum_b+=b[i];
	}
	if(sum_a>sum_b)return true;
	else if(sum_a==sum_b){
		for(int i=0;i<k;i++){
			if(a[i]>b[i])return true;
			else if(a[i]<b[i])return false;
		}
	}
	else return false;
}

void dfs(int index,int count,int sq_sum){
	if(count==k&&sq_sum==n){
		if(cmp(temp,s))for(int i=0;i<k;i++)s[i]=temp[i];
		flag=true;
		return;
	}
	if(count>k||sq_sum>n||index<1)return;
	temp[count]=index;
	dfs(index,count+1,sq_sum+int_power(index,p));
	dfs(index-1,count,sq_sum);
}
int main(){
	freopen("A1103.txt","r",stdin);
	scanf("%d%d%d",&n,&k,&p);
	dfs(sqrt(n),0,0);
	if(flag){
		for(int i=0;i<k;i++){
			if(i==0)printf("%d = %d^%d",n,s[i],p);
			else printf(" + %d^%d",s[i],p);
		}
	}
	else printf("Impossible");
	return 0;
}
