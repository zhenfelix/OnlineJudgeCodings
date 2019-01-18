#include<cstdio>
struct num{
	int g,s,k;
}a,b;
num add(num x,num y){
	num z;
	int temp,flag=0;
	temp=x.k+y.k;
	if(temp>=29){
		temp=temp-29;
		flag=1;
	}
	else flag=0;
	z.k=temp;
	temp=x.s+y.s+flag;
	if(temp>=17){
		temp=temp-17;
		flag=1;
	}
	else flag=0;
	z.s=temp;
	z.g=x.g+y.g+flag;
	return z;
}
int main(){
	freopen("A1058.txt","r",stdin);
	scanf("%d.%d.%d %d.%d.%d",&a.g,&a.s,&a.k,&b.g,&b.s,&b.k);
	num c=add(a,b);
	printf("%d.%d.%d",c.g,c.s,c.k);
	return 0;
}
