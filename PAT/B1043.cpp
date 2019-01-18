#include<cstdio>
#include<cstring>
int main(){
	freopen("B1043.txt","r",stdin);
	int HashTable[128]={0},i=0,count;
	char str[10010],mark[]="PATest",ch;
	gets(str);
	while(str[i]!='\0'){
		ch=str[i];
		HashTable[ch]++;
		i++;
	}
	do{
		count=0;
		for(i=0;i<6;i++){
			if(HashTable[mark[i]]>0)printf("%c",mark[i]),HashTable[mark[i]]--,count++;
		}
	}while(count>0);
	return 0;
}
