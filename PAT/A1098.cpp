#include<cstdio>
#include<algorithm>
using namespace std;
#define maxn 110
int origin[maxn],target[maxn],n;
bool insertion_sort(int a[]){
	bool flag=false;
	for(int i=2;i<=n;i++){
		for(int j=i-1;j>=1;j--){
			if(a[j]<=a[j+1])break;
			swap(a[j],a[j+1]);
		}
		if(flag){
			printf("Insertion Sort\n");
			for(int idx=1;idx<=n;idx++){
				printf("%d",a[idx]);
				if(idx<n)printf(" ");
			}
			return flag;
		}
		int k;
		for(k=n;k>=1;k--){
			if(a[k]!=target[k])break;
		}
		if(k<1)flag=true;
	}
	return flag;
}
void downadjust(int i,int end,int a[]){
	int j=i*2;
	while(j<=end){
			if(a[j+1]>a[j]&&j<end)j=j+1;
			if(a[i]>=a[j])break;
			swap(a[i],a[j]);
			i=j;
			j=i*2;
	}
}
void create_heap(int a[]){
	for(int i=n/2;i>=1;i--){
    downadjust(i,n,a);
	}
}
void heap_sort(int a[]){
	int end=n;
	bool flag=false;
	for(int end=n;end>1;end--){
		swap(a[1],a[end]);
		downadjust(1,end-1,a);
		if(flag){
			printf("Heap Sort\n");
			for(int idx=1;idx<=n;idx++){
				printf("%d",a[idx]);
				if(idx<n)printf(" ");
			}
			return;
		}
		int k;
	    for(k=1;k<=n;k++)if(a[k]!=target[k])break;
    	if(k>n)flag=true;
	}
	
}
int main(){
	freopen("A1098.txt","r",stdin);
	int a[maxn],b[maxn];
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		scanf("%d",&origin[i]);
		a[i]=origin[i];
		b[i]=origin[i];
	}
	for(int i=1;i<=n;i++)scanf("%d",&target[i]);
	if(insertion_sort(a))return 0;
	create_heap(b);
	heap_sort(b);
	
	return 0;
}
