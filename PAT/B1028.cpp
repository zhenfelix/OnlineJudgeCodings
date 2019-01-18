#include<cstdio>
struct Info{
	char name[10];
	int yy,mm,dd;
}young,old,left,right,temp;

bool More(Info a,Info b){
	if(a.yy!=b.yy)return a.yy<b.yy;
	else if(a.mm!=b.mm)return a.mm<b.mm;
	else if(a.dd!=b.dd)return a.dd<b.dd;
}

bool Less(Info a,Info b){
	if(a.yy!=b.yy)return a.yy>b.yy;
	else if(a.mm!=b.mm)return a.mm>b.mm;
	else if(a.dd!=b.dd)return a.dd>b.dd;
}

void init(){
	old.yy=right.yy=2014;
	young.yy=left.yy=1814;
	old.mm=young.mm=right.mm=left.mm=9;
	old.dd=young.dd=right.dd=left.dd=6;
}

int main(){
	init();
	int n,i,count=0;
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%s%d/%d/%d",&temp.name,&temp.yy,&temp.mm,&temp.dd);
		if(More(temp,right)&&Less(temp,left)){
			count++;
			if(More(temp,old))old=temp;
			if(Less(temp,young))young=temp;
		}
	}
	if(count==0)printf("0\n");
	else printf("%d %s %s\n",count,old.name,young.name);
	return 0;
}
