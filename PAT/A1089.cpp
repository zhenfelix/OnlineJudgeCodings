#include<cstdio>
#include<algorithm>
using namespace std;
#define maxn 110
int n,original[maxn],target[maxn];
bool merge_sort(int a[]){
	int num=2;
	bool flag=false;
	while(1){
		int left=0;
		for(;left<n;left+=num){
			int end=left+num;
			end=end>n?n:end;
			sort(a+left,a+end);
		}
		if(flag){
			printf("Merge Sort\n");
			for(int i=0;i<n;i++){
				printf("%d",a[i]);
				if(i<n-1)printf(" ");
			}
			break;
		}
		int k;
		for(k=0;k<n;k++)if(a[k]!=target[k]){
			break;
		}
		if(k>=n)flag=true;
		if(num>n)break;
		num*=2;
	}
	return flag;
}
void insertion_sort(int b[]){
	bool flag=false;
	for(int num=2;num<=n;num++){
		sort(b,b+num);
		if(flag){
			printf("Insertion Sort\n");
			for(int i=0;i<n;i++){
				printf("%d",b[i]);
				if(i<n-1)printf(" ");
			}
			break;
		}
		int k;
		for(k=0;k<n;k++)if(b[k]!=target[k]){
			break;
		}
		if(k>=n)flag=true;
	}
}
int main(){
	freopen("A1089.txt","r",stdin);
	int a[maxn],b[maxn];
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		scanf("%d",&original[i]);
		a[i]=original[i];
		b[i]=original[i];
	}
	for(int i=0;i<n;i++)scanf("%d",&target[i]);
	if(merge_sort(a))return 0;
	insertion_sort(b);
	return 0;
}
