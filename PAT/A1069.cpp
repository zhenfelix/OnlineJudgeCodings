#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;
#define N 4
int Minus(int a[],int b[]){
	int sum=0;
	for(int i=N-1;i>=0;i--){
		if(a[i]<b[i]){
			a[i-1]--;
			a[i]=a[i]+10-b[i];
		}
		else a[i]=a[i]-b[i];
		sum+=a[i]*pow(10,N-1-i);
	}
	return sum;
}
void intcpy(int x[],int y[]){
	for(int i=0;i<N;i++)x[i]=y[i];
}
bool cmpde(int x,int y){
	return x>y;
}
void str2int(int x[],char y[]){
	for(int i=0;i<N;i++)x[i]=y[i]-'0';
}
void intprint(int x[]){
	for(int i=0;i<N;i++)printf("%d",x[i]);
}
int main(){
	freopen("A1069.txt","r",stdin);
	int a[N],b[N],k;
	char x[10];
	gets(x);
	str2int(a,x);
	intcpy(b,a);
	do{
		sort(a,a+N,cmpde);
		sort(b,b+N);
		intprint(a);
		printf(" - ");
		intprint(b);
		printf(" = ");
		k=Minus(a,b);
		intprint(a);printf("\n");
		if(k==0)break;
		intcpy(b,a);
	}while(k!=6174);
	return 0;
}
