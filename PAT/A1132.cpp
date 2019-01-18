#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
const int nmax=25;
char str[nmax];

long long str2int(int xyz[],int len){
	long long sum=0;
	for(int i=0;i<len;i++){
		sum=sum*10+xyz[i];
	}
	return sum;
}
void read_data(){
	int n,nh;
	int x[nmax],a[nmax],b[nmax];
	bool flag=false;
	gets(str);
	n=strlen(str);nh=n/2;
	for(int i=0;i<n;i++)x[i]=str[i]-'0';
	for(int i=0;i<nh;i++)a[i]=str[i]-'0';
	for(int i=nh;i<n;i++)b[i-nh]=str[i]-'0';
	long long temp=(str2int(b,nh)*str2int(a,nh));
	long long t=str2int(x,n);
	if(temp==0)flag=false;
	else if(t%temp==0)flag=true;
	if(flag)printf("Yes\n");
	else printf("No\n");
	return;
}
int main(){
	//freopen("a.txt","r",stdin);
	int num;
	scanf("%d\n",&num);
	for(int i=0;i<num;i++){
		read_data();
	}
	return 0;
}
