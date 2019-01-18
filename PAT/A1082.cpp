#include<cstdio>
#include<cstring>
int main(){
	freopen("A1082.txt","r",stdin);
	char num[15],*p,mark[][10]={"ling","yi","er","san","si","wu","liu","qi","ba","jiu"};
	char level[4][10]={"","Shi","Bai","Qian"};
	int i,len;
	bool flag=false,first=true;
	gets(num);len=strlen(num);p=num;
	if(num[0]=='-')printf("Fu "),p++,len--;
	if(*p=='0'){
		printf("ling");
		return 0;
	}
	for(i=len;i>0;i--){
		if(*(p+len-i)=='0'&&flag==false)flag=true;
		else if(*(p+len-i)=='0'&&flag==true);
		else {
			if(flag==true)printf(" %s",mark[0]);
			flag=false;
			if(first)printf("%s",mark[*(p+len-i)-'0']),first=false;
			else printf(" %s",mark[*(p+len-i)-'0']);
			if((i-1)%4>0&&(i-1)%4<4)printf(" %s",level[(i-1)%4]);
		}
		if(i==9)printf(" Yi");
		if(i==5)printf(" Wan");
	}
	return 0;
}
