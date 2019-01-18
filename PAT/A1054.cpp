#include<cstdio>
int main(){
	freopen("A1054.txt","r",stdin);
	int n,m,count=0,ans,temp;
	scanf("%d%d",&n,&m);
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			scanf("%d",&temp);
			if(count==0)ans=temp;
			else{
				if(ans==temp)count++;
				else count--;
			}
		}
	}
	printf("%d",ans);
}
