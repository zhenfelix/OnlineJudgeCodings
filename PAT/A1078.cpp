#include<cstdio>
#include<cmath>
using namespace std;
bool HashTable[10010]={0};
bool IsPrime(int x){
	if(x<=1)return false;
	int sqr=sqrt(x*1.0);
	for(int i=2;i<=sqr;i++){
		if(x%i==0)return false;
	}
	return true;
}
int main(){
	freopen("A1078.txt","r",stdin);
	int m,n,temp,idx;
	scanf("%d%d",&m,&n);
	while(!IsPrime(m))m++;
	for(int i=0;i<n;i++){
		scanf("%d",&temp);
		idx=temp%m;
		if(!HashTable[idx]){
			printf("%d",idx);
			HashTable[idx]=true;
		}
		else{
			int step=1;
			while(1){
				idx=(temp+step*step)%m;
				if(step>=m){
					printf("-");
					break;
				}
				else if(!HashTable[idx]){
					printf("%d",idx);
					HashTable[idx]=true;
					break;
				}
				
				step++;
			}
			
		}
		if(i<n-1)printf(" ");
	}
	return 0;
}
