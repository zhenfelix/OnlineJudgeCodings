#include<cstdio>
#include<algorithm>
#define MAXN 100010
using namespace std;
int main(){
	freopen("A1037.txt","r",stdin);
	int nc,np,c[MAXN],p[MAXN],ans=0;
	scanf("%d",&nc);
	for(int i=0;i<nc;i++)scanf("%d",&c[i]);
	scanf("%d",&np);
	for(int i=0;i<np;i++)scanf("%d",&p[i]);
	sort(c,c+nc);
	sort(p,p+np);
	for(int i=0;i<nc&&i<np;i++){
		if(c[i]<0&&p[i]<0)ans+=c[i]*p[i];
		if(c[nc-1-i]>0&&p[np-1-i]>0)ans+=c[nc-1-i]*p[np-1-i];
	}
	printf("%d",ans);
	return 0;
}
