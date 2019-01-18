#include<cstdio>
#include<cstring>
struct user{
	char name[15],psw[15];
}a[1010];
bool modify(struct user &x){
	int i,len;
	bool flag=false;
	len=strlen(x.psw);
	for(i=0;i<len;i++){
		if(x.psw[i]=='1')x.psw[i]='@',flag=true;
		else if(x.psw[i]=='l')x.psw[i]='L',flag=true;
		else if(x.psw[i]=='0')x.psw[i]='%',flag=true;
		else if(x.psw[i]=='O')x.psw[i]='o',flag=true;
	}
	return flag;
}
int main(){
	freopen("A1035.txt","r",stdin);
	struct user x;
	int n,m=0,j=0,i;
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%s %s",x.name,x.psw);
		if(modify(x))a[j++]=x;
	}
	if(j>0)printf("%d\n",j);
	else if(j==0&&n==1)printf("There is 1 account and no account is modified\n");
	else printf("There are %d accounts and no account is modified\n",n);

	for(i=0;i<j;i++)printf("%s %s\n",a[i].name,a[i].psw);
	return 0;
}
