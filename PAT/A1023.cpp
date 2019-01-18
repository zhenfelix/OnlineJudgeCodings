#include<cstdio>
#include<cstring>
#define num 25
using namespace std;
char a[num],q[num]={'0'};
int HashTable[10]={0};
void reverse(char x[],int len){
	char temp;
	for(int i=0;i<len/2;i++){
		temp=x[i];
		x[i]=x[len-1-i];
		x[len-1-i]=temp;
	}
}
void init(){
	for(int i=0;i<num;i++){
		q[i]='0';
	}
}
int main(){
	freopen("A1023.txt","r",stdin);
	int x,len,count;
	bool flag=true;
	init();
	scanf("%s",a);
	len=strlen(a);
	reverse(a,len);
	for(int i=0;i<len;i++){
		x=a[i]-'0';
		HashTable[x]++;
		x=2*x;
		q[i]=q[i]+x%10;
		q[i+1]=q[i+1]+x/10;
	}
	
	if(q[len]!='0')count=len+1;
	else count=len;
	
	reverse(q,count);
	for(int i=0;i<count;i++){
		x=q[i]-'0';
		HashTable[x]--;
		if(HashTable[x]<0){
			flag=false;
			break;
		}
	}
	if(flag)printf("Yes\n");
	else printf("No\n");
	for(int i=0;i<count;i++)printf("%c",q[i]);
	return 0;
}
