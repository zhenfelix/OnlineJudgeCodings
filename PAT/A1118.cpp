#include<cstdio>
#define N 10010
int pic[N],bird2pic[N]={0},n,q;
void init(){
	for(int i=1;i<=n;i++)pic[i]=i;
}
int find_root(int p){
	if(pic[p]==p)return p;
	int F=find_root(pic[p]);
	pic[p]=F;
	return F;
}
void merge(int x,int y){
	x=find_root(x);
	y=find_root(y);
	pic[x]=y;
}
int main(){
	freopen("A1118.txt","r",stdin);
	int numT=0,numB=0;
	scanf("%d",&n);
	init();
	for(int i=1;i<=n;i++){
		int k;
		scanf("%d",&k);
		for(int j=1;j<=k;j++){
			int temp;
			scanf("%d",&temp);
			if(bird2pic[temp]==0){
				bird2pic[temp]=i;
				numB++;
			}
			else{
				merge(i,bird2pic[temp]);
//				for(int s=1;s<=n;s++)printf("%d ",pic[s]);
//				printf("\n");
			}
		}
	}
	for(int i=1;i<=n;i++){
		if(pic[i]==i)numT++;
	}
	printf("%d %d\n",numT,numB);
	int a,b;
	scanf("%d",&q);
	for(int i=0;i<q;i++){
		scanf("%d%d",&a,&b);
		if(find_root(bird2pic[a])==find_root(bird2pic[b]))printf("Yes\n");
		else printf("No\n");
	}
	return 0;
}
