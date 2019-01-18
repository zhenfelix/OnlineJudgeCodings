#include<cstdio>
#include<algorithm>
using namespace std;
#define maxn 10
int str2num(int a[],int len){
	int ans=0;
	for(int i=0;i<len;i++){
		ans=ans*10+a[i];
	}
	return ans;
}
void num2str(int x,int a[],int len){
	for(int i=0;i<len;i++){
		a[i]=x%10;
		x=x/10;
	}
}
bool cmp(int a,int b){
	return a>b;
}
int main(){
	freopen("A1069.txt","r",stdin);
	int x,a[maxn],b[maxn],len=4,left,right,diff;
	scanf("%d",&x);
	diff=x;
	while(1){
		num2str(diff,a,len);
		num2str(diff,b,len);
		sort(a,a+len,cmp);
		sort(b,b+len);
		left=str2num(a,len);
		right=str2num(b,len);
		diff=left-right;
		printf("%04d - %04d = %04d\n",left,right,diff);
		if(diff==0||diff==6174)break;
	}
	return 0;
}
