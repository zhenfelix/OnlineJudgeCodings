#include<cstdio>
#include<cstring>
#define N 110

void reverse(char *p, int n){
	int i;
	char temp;
	for(i=0;i<n/2;i++){
		temp=p[i];
		p[i]=p[n-1-i];
		p[n-1-i]=temp;
	}
}
int main(){
	freopen("B1048.txt","r",stdin);
	char a[N],b[N],mark[15]="0123456789JQK";
	int i,n1,n2,len,s,le;
	scanf("%s %s",a,b);
	n1=strlen(a),n2=strlen(b);
	reverse(a,n1);reverse(b,n2);
	len=n1>n2?n1:n2;
	le=n1<n2?n1:n2;
	if(n1<n2)for(i=le;i<len;i++)a[i]='0';
	else for(i=le;i<len;i++)b[i]='0';
	for(i=0;i<len;){
		b[i]=mark[(a[i]-'0'+b[i]-'0')%13];
		if(i<len-1){
			s=b[i+1]-a[i+1];
		    if(s<0)s+=10;
	    	b[i+1]=s+'0';
		}
		i+=2;
	}
	reverse(b,len);
	printf("%s",b);
	return 0;
}
