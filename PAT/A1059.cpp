#include<cstdio>
#include<cmath>
using namespace std;
int main(){
	freopen("A1059.txt","r",stdin);
	int x,sq,count;
	bool flag=false;
	scanf("%d",&x);
	printf("%d=",x);
	sq=(int)sqrt(x*1.0);
	for(int i=2;i<=sq;){
		if(x%i==0){
			if(flag)printf("*");
			flag=true;
			count=0;
			while(x%i==0){
				count++;
				if(count==1)printf("%d",i);
				x=x/i;
			}
			if(count>1)printf("^%d",count);
		}
		if(i==2)i++;
		else i=i+2;
	}
	if(x!=1){
		if(flag)printf("*");
		printf("%d",x);
	}
	else if(x==1&&!flag)printf("1");
	return 0;
}
