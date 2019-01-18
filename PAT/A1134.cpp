#include<cstdio>
#include<vector>
using namespace std;
const int nmax=10010;
bool vs[nmax]={false};
int G[nmax][2];

int main(){
	//freopen("c.txt","r",stdin);
	int n,m,k,nv;
	scanf("%d%d",&n,&m);
	for(int i=0;i<m;i++){
		scanf("%d%d",&G[i][0],&G[i][1]);
	}
	scanf("%d",&k);
	for(int i=0;i<k;i++){
		scanf("%d",&nv);
		for(int j=0;j<nv;j++){
			int temp;
			scanf("%d",&temp);
			vs[temp]=true;
		}
		int j;
		for(j=0;j<m;j++){
			if(vs[G[j][0]]==false&&vs[G[j][1]]==false)break;
		}
		if(j<m)printf("No\n");
		else printf("Yes\n");
		for(int v=0;v<n;v++)vs[v]=false;
	}
}
