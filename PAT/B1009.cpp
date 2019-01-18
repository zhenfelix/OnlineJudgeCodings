#include<cstdio>
#include<cstring>
int main(){
	freopen("B1009.txt","r",stdin);
	char str[100],word[80][80];
	int i,j=0,k=0,len;
	gets(str);
	len=strlen(str);
	for(i=0;i<len;i++){
		if(str[i]!=' ')word[j][k++]=str[i];
		else {
			word[j++][k]='\0';
			k=0;
		}
	}
	for(i=j;i>=0;i--){
		printf("%s",word[i]);
		if(i!=0)printf(" ");
	}
	return 0;
		
}
