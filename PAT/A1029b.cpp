#include<cstdio>
#define maxn 1000010
int a[maxn],b[maxn],n,m;
const int inf=(1<<31)-1;
int main(){
	freopen("A1029.txt","r",stdin);
	scanf("%d",&n);
	for(int i=0;i<n;i++)scanf("%d",&a[i]);
	a[n]=inf;
	scanf("%d",&m);
	for(int i=0;i<m;i++)scanf("%d",&b[i]);
	int count=-1,i=0,j=0,temp;
	int median=(n+m-1)/2;
	for(;i<n+1;i++){
		for(;b[j]<a[i]&&j<m;j++){
			temp=b[j];
			count++;
			if(count==median){
				printf("%d",temp);
				return 0;
			}
		}
		temp=a[i];
		count++;
		if(count==median){
			printf("%d",temp);
			return 0;
		}
	}
	return 0;
}
