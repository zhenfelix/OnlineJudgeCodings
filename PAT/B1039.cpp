#include<cstdio>
#include<cstring>
int HashTable[128]={0};
int main(){
	freopen("A1092.txt","r",stdin);
	int i,count=0,len;
	char str[1010];
	gets(str);
	len=strlen(str);
	for(i=0;i<len;i++)HashTable[str[i]]++;
	gets(str);
	i=0;
	bool flag=true;
	while(str[i]!='\0'){
		if(HashTable[str[i]]!=0)HashTable[str[i]]--,len--;
		else flag=false,count++;
		i++;
	}
	if(flag)printf("Yes %d",len);
	else printf("No %d",count);
	return 0;
}
