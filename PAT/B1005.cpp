#include<cstdio>
using namespace std;
int HashTable[110]={0};
void calz(int x){
	int y;
	if(x>1){
		if(x%2==0)y=x/2;
    	else y=(3*x+1)/2;
	}
	else y=x;
	if(y<101)if(HashTable[y]!=1)HashTable[y]=1,calz(y);
	else if(y>=101)calz(y);
	//printf("%d %d\n",y,HashTable[y]);
	//,printf("%d %d\n",y,HashTable[y])
}

int main(){
	freopen("B1005.txt","r",stdin);
	int temp=0,k,i,x;
	scanf("%d",&k);
	for(i=0;i<k;i++){
		scanf("%d",&x);
		if(HashTable[x]==0)HashTable[x]=-1;
		calz(x);
		if(x>temp)temp=x;
	}
	int count=0,j=0;
	for(i=temp;i>=1;i--){
		if(HashTable[i]==-1)count++;
	}
	for(i=temp;i>=1;i--){
		if(HashTable[i]==-1){
			printf("%d",i);
			if(j!=count-1)printf(" "),j++;
		}
		
	}
	return 0;
}
