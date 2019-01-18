#include<cstdio>
int main(){
	freopen("B1006.txt","r",stdin);
	int n,i,j=0,r,level=0,count=0;
	char p[30],mark[]="0123456789";
	scanf("%d",&n);
	do{
		r=n%10;
		n=n/10;
		for(i=0;i<r;i++){
			count++;
			if(level==0)p[i+j]=mark[r-i];
			else if(level==1)p[i+j]='S';
			else p[i+j]='B';
		};
		j+=i;
	    level++;
	}while(n!=0);
	for(i=count-1;i>=0;i--)printf("%c",p[i]);
	return 0;
}
