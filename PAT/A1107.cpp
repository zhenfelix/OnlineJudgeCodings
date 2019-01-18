#include<cstdio>
#include<map>
#include<algorithm>
using namespace std;
#define maxn 1010
int ans[maxn],n,father[maxn],num[maxn];
map<int,int> cluster;
void init(){
	for(int i=1;i<=n;i++)father[i]=i;
}
int find_root(int root){
	if(father[root]==root)return root;
	int F=find_root(father[root]);
	father[root]=F;
	return F;
}
void unite(int a,int b){
	int fa,fb;
	fa=find_root(a),fb=find_root(b);
	if(fa!=fb){
		father[father[b]]=fa;
	}
}
bool cmp(int a,int b){
	return a>b;
}
int main(){
	freopen("A1107.txt","r",stdin);
	int k,a,b;
	scanf("%d",&n);
	init();
	for(int i=1;i<=n;i++){
		scanf("%d: %d",&k,&a);
		find_root(a);
		ans[i]=a;
		if(k>1){
			for(int j=1;j<k;j++){
				scanf("%d",&b);
				unite(a,b);
			}
		}
	}
	for(int i=1;i<=n;i++){
		int root=find_root(ans[i]);
		if(cluster.find(root)!=cluster.end())cluster[root]++;
		else cluster[root]=1;
	}
	int count=0;
	for(map<int,int>::iterator it=cluster.begin();it!=cluster.end();it++){
		num[count++]=it->second;
	}
	sort(num,num+n,cmp);
	printf("%d\n",count);
	for(int i=0;i<count;i++){
		printf("%d",num[i]);
		if(i<count-1)printf(" ");
	}
	return 0;
}
