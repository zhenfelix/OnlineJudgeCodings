#include<cstdio>
int main(){
	freopen("B1038.txt","r",stdin);
	int n,k,HashTable[110]={0},score;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		scanf("%d",&score);
		HashTable[score]++;
	}
	scanf("%d",&k);
	for(int i=0;i<k;i++){
		scanf("%d",&score);
		printf("%d",HashTable[score]);
		if(i<k-1)printf(" ");
	}
	return 0;
}
