#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
struct seg{
	char str[10];
}s[10010];
bool cmp(seg a,seg b){
	char temp1[20],temp2[20];
	strcpy(temp1,a.str);strcat(temp1,b.str);
	strcpy(temp2,b.str);strcat(temp2,a.str);
	return strcmp(temp1,temp2)<0;
}
int main(){
	freopen("A1038.txt","r",stdin);
	int n;
	scanf("%d ",&n);
	for(int i=0;i<n;i++)scanf("%s",s[i].str);
	sort(s,s+n,cmp);
	bool flag=true;
	for(int i=0;i<n;i++)for(int j=0;j<strlen(s[i].str);j++){
		if(s[i].str[j]=='0'&&flag)continue;
		else printf("%c",s[i].str[j]),flag=false;
	}
	if(flag)printf("%d",0);
	return 0;
}
