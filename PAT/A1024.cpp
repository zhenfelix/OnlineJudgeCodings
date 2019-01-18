#include<cstdio>
#include<cstring>
#define num 100
using namespace std;
char s[num],sp[num];

bool judge(char s[],int len){
	for(int i=0;i<len/2;i++){
		if(s[i]!=s[len-1-i])return false;
	}
	return true;
}
void reverse(char x[],int len){
	char temp;
	for(int i=0;i<len/2;i++){
		temp=x[i];
		x[i]=x[len-1-i];
		x[len-1-i]=temp;
	}
}
int add(char a[],char b[],int len){
	int temp,count;
	for(count=0;count<len;count++){
		temp=a[count]-'0'+b[count]-'0';
		a[count]=temp%10+'0';
		if(count<len-1)a[count+1]+=temp/10;
		else a[count+1]=temp/10+'0';
	}
	if(a[count]!='0')return len+1;
	else{
		a[count]='\0';
		return len;
	}
}

int main(){
	freopen("A1024.txt","r",stdin);
	int k,len,temp,i;
	scanf("%s%d",s,&k);
	for(i=0;i<k;i++){
		len=strlen(s);
		if(judge(s,len))break;
		strcpy(sp,s);
		reverse(s,len);
		len=add(s,sp,len);
		reverse(s,len);
	}
	printf("%s\n%d",s,i);
}
