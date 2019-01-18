#include<cstdio>
int main(){
	freopen("A1048.txt","r",stdin);
	int coin[510]={0},i,n,m,temp;
	bool flag=false;
	scanf("%d%d",&n,&m);
	for(i=0;i<n;i++)scanf("%d",&temp),coin[temp]++;
	for(i=1;i<=m/2;i++){
		if(coin[i]>0&&coin[m-i]>0){
			if(i==m-i&&coin[i]>1){
				printf("%d %d",i,i);
				flag=true;
				break;
			}
			else if(i<m-i){
				printf("%d %d",i,m-i);
				flag=true;
				break;
			} 
		}
	}
	if(flag==false)printf("No Solution");
	return 0;
}
