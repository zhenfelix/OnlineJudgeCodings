#include<cstdio>
#include<cstring>
bool check(char *p){
	int i,sum=0,w[]={7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2};
	char m[]={'1','0','X','9','8','7','6','5','4','3','2'};
	for(i=0;i<17;i++)if(p[i]-'0'<0||p[i]-'0'>9)return false;
	for(i=0;i<17;i++)sum+=((p[i]-'0')*w[i]);
	if(m[(sum%11)]==p[17])return true;
	else return false;
}
int main(){
	freopen("B1031.txt","r",stdin);
	int N,i,count=0,len;
	char id[20];
	scanf("%d\n",&N);
	for(i=0;i<N;i++){
		gets(id);
		if(check(id)==true)count++;
		else printf("%s\n",id);
	}
	if(count==N)printf("All passed\n");
	return 0;
}
