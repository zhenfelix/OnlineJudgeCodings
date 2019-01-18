#include<cstdio>
struct rational{
	long long up,down;
};
long long gcd(long long a,long long b){
	return b==0?a:gcd(b,a%b);
}
rational add(rational a,rational b){
	rational c;
	c.down=a.down*b.down;
	c.up=a.up*b.down+b.up*a.down;
	return c;
}
rational minus(rational a,rational b){
	rational c;
	c.down=a.down*b.down;
	c.up=a.up*b.down-b.up*a.down;
	return c;
}
rational multiply(rational a,rational b){
	rational c;
	c.down=a.down*b.down;
	c.up=a.up*b.up;
	return c;
}
rational divide(rational a,rational b){
	rational c;
	c.down=a.down*b.up;
	c.up=a.up*b.down;
	return c;
}
void show(rational a){
	bool flag=false;
	long long x,y,z=0;
	x=a.up,y=a.down;
	if(y<0)y=-y,x=-x;
	if(y==0){
		printf("Inf");
		return;
	}
	else if(x==0){
		printf("0");
		return;
	}
	else{
		if(x<0){
			flag=true;
			x=-x;
		}
		if(flag)printf("(-");
		long long temp=gcd(x,y);
		x/=temp,y/=temp;
		z=x/y,x=x%y;
		if(z>0)printf("%lld",z);
		if(z>0&&x!=0)printf(" ");
		if(x!=0)printf("%lld/%lld",x,y);
		if(flag)printf(")");
		return;
	}
}
int main(){
	freopen("A1088.txt","r",stdin);
	freopen("A1088-out.txt","w",stdout);
	rational a,b;
	scanf("%lld/%lld %lld/%lld",&a.up,&a.down,&b.up,&b.down);
	show(a);printf(" + ");show(b);printf(" = ");show(add(a,b));printf("\n");
	show(a);printf(" - ");show(b);printf(" = ");show(minus(a,b));printf("\n");
	show(a);printf(" * ");show(b);printf(" = ");show(multiply(a,b));printf("\n");
	show(a);printf(" / ");show(b);printf(" = ");show(divide(a,b));printf("\n");
	return 0;
}
