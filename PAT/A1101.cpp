#include<cstdio>
#include<algorithm>
using namespace std;
#define inf 1000000001
int a[100010],leftmax[100010],rightmin[100010],x[100010];
int main(){
	freopen("A1101.txt","r",stdin);
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++)scanf("%d",&a[i]);
	leftmax[0]=0;
	for(int i=1;i<n;i++){
		if(a[i-1]>leftmax[i-1])leftmax[i]=a[i-1];
		else leftmax[i]=leftmax[i-1];
	}
	rightmin[n-1]=inf;
	for(int i=n-2;i>=0;i--){
		if(a[i+1]<rightmin[i+1])rightmin[i]=a[i+1];
		else rightmin[i]=rightmin[i+1];
	}
	int count=0;
	for(int i=0;i<n;i++){
		if(a[i]>leftmax[i]&&a[i]<rightmin[i])x[count++]=a[i];
	}
	printf("%d\n",count);
	//sort(x,x+count);
	for(int i=0;i<count;i++){
		printf("%d",x[i]);
		if(i!=count-1)printf(" ");
	}
	printf("\n");
	return 0;
}
