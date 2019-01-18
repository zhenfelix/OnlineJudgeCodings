#include<cstdio>
#include<algorithm>
using namespace std;
int HashTable[100010];

int main(){
	freopen("A1067.txt","r",stdin);
	int n,ans=0,perm=0,temp,num;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		scanf("%d",&num);
		HashTable[num]=i;
		if(i!=num)perm++;
	}
	int j=1;
	while(perm>0){
		if(HashTable[0]!=0){
			swap(HashTable[0],HashTable[HashTable[0]]);
			perm--;
			ans++;
			if(HashTable[0]==0)perm--;
		}
		else{
			for(;j<n;j++)if(HashTable[j]!=j){
				swap(HashTable[0],HashTable[j]);
				perm++;
				ans++;
				break;
			}
		}
	}
	printf("%d",ans);
	return 0;
}
