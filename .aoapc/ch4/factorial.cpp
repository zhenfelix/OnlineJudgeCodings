#include<cstdio>
int f(int t){
	if(t==0)return 1;
	return t*f(t-1);
}
int main(){
	int x;
	scanf("%d",&x);
	printf("%d\n",f(x));
	return 0;
}
