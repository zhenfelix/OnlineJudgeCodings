#include<cstdio>
int HashTable[10]={0};

int main(){
	freopen("B1023.txt","r",stdin);
	for(int i=0;i<10;i++)scanf("%d",&HashTable[i]);
	for(int i=1;i<10;i++)if(HashTable[i]!=0){
		printf("%d",i);
		HashTable[i]--;
		break;
	}
	for(int i=0;i<10;i++)while(HashTable[i]!=0)printf("%d",i),HashTable[i]--;
	return 0;
}
