#include<cstdio>
#include<cstring>
int main(){
	freopen("B1042.txt","r",stdin);
	int HashTable[128]={0},i=0,temp=0;
	char str[1010],ch,id;
	gets(str);
	while(str[i]!='\0'){
		ch=str[i];
		if(ch>='A'&&ch<='Z')HashTable['a'+ch-'A']++;
		else if(ch>='a'&&ch<='z')HashTable[ch]++;
		i++;
	}
	for(ch='a';ch<='z';ch++){
		if(HashTable[ch]>temp)id=ch,temp=HashTable[ch];
	}
	printf("%c %d",id,temp);
	return 0;
}
