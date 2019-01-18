#include<cstdio>
#include<cstring>
char cc(char a){
	char c;
	if(a>='a'&&a<='z')c=a-'a'+'A';
	else c=a;
	return c;
}
int main(){
	freopen("B1029.txt","r",stdin);
	bool HashTable[128]={false};
	char str1[100],str2[100],a,b;
	int len1,len2,i,j;
	gets(str1);
	gets(str2);
	len1=strlen(str1),len2=strlen(str2);
	for(i=0,j=0;i<len1;i++){
		a=str1[i],b=str2[j];
		a=cc(a),b=cc(b);
		if(a!=b&&HashTable[a]==false)printf("%c",a),HashTable[a]=true;
		else if(a==b)j++;
	}
	return 0;
}
