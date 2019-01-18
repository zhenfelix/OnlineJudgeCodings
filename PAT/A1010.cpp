#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
typedef long long LL;
char n1[15],n2[15];
int mark[256],radix,tag;
void init(){
	char c;
	for(c='0';c<='9';c++)mark[c]=c-'0';
	for(c='a';c<='z';c++)mark[c]=c-'a'+10;
}
LL compute(char x[],int r){
	int len;
	LL ans=0;
	len=strlen(x);
	for(int i=0;i<len;i++)ans=ans*r+mark[x[i]];
	return ans;
}
int cmp(char x[],LL r,LL t){
	LL num=compute(x,r);
	if(num<0)return 1;
	if(num<t)return -1;
	else if(num==t)return 0;
	else return 1;
}
int binsrch(LL t,char y[],LL low,LL high){
	LL mid;
	while(low<=high){
		mid=(low+high)/2;
		int m=cmp(y,mid,t);
		if(m<0)low=mid+1;
		else if(m>0)high=mid-1;
		else return mid;
	}
	return -1;
}
int main(){
	freopen("A1010.txt","r",stdin);
	init();
	char temp[15];
	LL low=0,high,t;
	int ans;
	scanf("%s %s %d%d",n1,n2,&tag,&radix);
	if(tag==2){
		strcpy(temp,n1);
		strcpy(n1,n2);
		strcpy(n2,temp);
	}
	t=compute(n1,radix);
	for(int i=0;i<strlen(n2);i++)if(mark[n2[i]]>low)low=mark[n2[i]];
	low++;
	high=max(low,t)+1;
	ans=binsrch(t,n2,low,high);
	if(ans==-1)printf("Impossible");
	else printf("%lld",ans);
	return 0;
}
