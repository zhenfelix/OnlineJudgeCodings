#include<cstdio>
double a[100010],sum=0;
int main(){
	freopen("A1104.txt","r",stdin);
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		scanf("%lf",&a[i]);
		sum+=a[i]*(i+1)*(n-i);
	}
	printf("%.2f",sum);
	return 0;
}
