#include<cstdio>
#include<cstring>
bool ischar(char c, int type){
	if(c-'A'>=0&&c-'A'<7&&type==0)return true;
	else if(((c-'A'>=0&&c-'A'<14)||(c-'0'>=0&&c-'0'<10))&&type==1)return true;
	else if(((c-'A'>=0&&c-'A'<26)||(c-'a'>=0&&c-'a'<26))&&type==2)return true;
	else return false;
}
int com(char *a, char *b, int x, int y,int *ans, int type){
	int i,j;
	for(i=0;i<x&&i<y;i++){
		if(a[i]==b[i]&&ischar(a[i],type)){
			ans[0]=i;
			ans[1]=i;
			return 0;
		}
	}
}
int main(){
	freopen("B1014.txt","r",stdin);
	char a[70],b[70],day[7][10]={"MON","TUE","WED","THU","FRI","SAT","SUN"};
	char hour[24];
	int x,y,ans[6],i;
	for(i=0;i<24;i++){
		if(i<10)hour[i]='0'+i;
		else hour[i]='A'+i-10;
	}
	gets(a);gets(b);
	x=strlen(a);y=strlen(b);
	com(a,b,x,y,ans,0);
	printf("%s ",day[a[ans[0]]-'A']);
	com(a+ans[0]+1,b+ans[0]+1,x-1-ans[0],y-1-ans[1],ans+2,1);
	for(i=0;i<24;i++)if(hour[i]==a[ans[0]+ans[2]+1])break;
	printf("%02d:",i);
	gets(a);gets(b);
	x=strlen(a);y=strlen(b);
	com(a,b,x,y,ans+4,2);
	printf("%02d",ans[5]);
	return 0;
}
