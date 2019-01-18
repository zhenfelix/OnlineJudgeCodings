#include<cstdio>
void convert(char *p,char *mark, int x){
	do{
		*(p++)=mark[x%13];
		x=x/13;
	}while(x!=0);
}
int main(){
	freopen("A1027.txt","r",stdin);
	int R,G,B,i,j;
	char mark[13],M[]={'A','B','C'},r[]="00",g[]="00",b[]="00";
	for(i=0;i<10;i++)mark[i]=i+'0';
	for(j=0;j<3;j++)mark[i+j]=M[j];
	scanf("%d%d%d",&R,&G,&B);
	convert(r,mark,R);convert(g,mark,G);convert(b,mark,B);
	printf("#%c%c%c%c%c%c",r[1],r[0],g[1],g[0],b[1],b[0]);
	return 0;
	
}
