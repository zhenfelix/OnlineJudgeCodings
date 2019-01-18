#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
#define maxn 1010
#define maxk 1010
int n,user[maxn],hobby[maxk],Hashmap[maxn]={0};
vector<int>a;
void init(){
	for(int i=1;i<=n;i++)user[i]=i;
	for(int i=0;i<maxk;i++)hobby[i]=0;
}
int find_root(int node){
	if(node==user[node])return node;
	else {
		int root;
    	root=find_root(user[node]);
    	user[node]=root;
    	return root;
	}
	
}
void merge(int x,int y){
	x=find_root(x);
	y=find_root(y);
	if(x!=y)user[x]=y;
}
bool cmp(int x,int y){
	return x>y;
}
int main(){
	freopen("A1107.txt","r",stdin);
	scanf("%d",&n);
	init();
	for(int i=1;i<=n;i++){
		int k;
		scanf("%d:",&k);
		for(int j=1;j<=k;j++){
			int temp;
			scanf("%d",&temp);
			if(hobby[temp]==0)hobby[temp]=i;
			else{
				merge(hobby[temp],i);
			}
//			for(int t=1;t<=n;t++)printf("%d ",user[t]);
//			printf("-> cycle: %d\n",j);
		}
	}
	for(int i=1;i<=n;i++){
		Hashmap[find_root(i)]++;
	}
	for(int i=1;i<=n;i++){
		if(Hashmap[i]>0)a.push_back(Hashmap[i]);
	}
	sort(a.begin(),a.end(),cmp);
	printf("%d\n",a.size());
	printf("%d",a[0]);
	for(int i=1;i<a.size();i++){
		printf(" %d",a[i]);
	}
}
