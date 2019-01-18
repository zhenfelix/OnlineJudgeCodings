#include<cstdio>
#include<algorithm>
using namespace std;
bool HashTable[100]={0};
int n,a[100],b[100];
void generate(int index){
	if(index<n){
		for(int i=0;i<n;i++){
			if(!HashTable[i])b[index]=a[i],HashTable[i]=true,generate(index+1),HashTable[i]=false;
		}
	}
	else{
		for(int i=0;i<n;i++)printf("%d ",b[i]);
		printf("\n");
	}
}
int main(){
	freopen("permutation.txt","r",stdin);
//	freopen("permutation_out.txt","w",stdout);
	scanf("%d",&n);
	for(int i=0;i<n;i++)scanf("%d",&a[i]);
	sort(a,a+n);
	for(int i=0;i<n;i++)printf("%d ",a[i]);printf("\n");
	generate(0);
	return 0;
}
