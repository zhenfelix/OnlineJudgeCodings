#include<cstdio>
#include<cstring>
struct TimeStamp{
	int hh,mm,ss;
}t_max,t_min,temp1,temp2;
bool More(TimeStamp a, TimeStamp b)
{
	if(a.hh!=b.hh)return a.hh>b.hh;
	else if(a.mm!=b.mm)return a.mm>b.mm;
	else if(a.ss!=b.ss)return a.ss>b.ss;
}
void init()
{
	t_max.hh=0,t_max.mm=0,t_max.ss=0;
	t_min.hh=23,t_min.mm=59,t_min.ss=59;
}
int main()
{
	freopen("A1006.txt", "r", stdin);
	init();
	int m,i;
	char id_temp[20],id_max[20],id_min[20];
	scanf("%d",&m);
	for(i=0;i<m;i++){
		scanf("%s %d:%d:%d %d:%d:%d",id_temp,&temp1.hh,&temp1.mm,&temp1.ss,&temp2.hh,&temp2.mm,&temp2.ss);
		if(More(t_min,temp1))t_min=temp1,strcpy(id_min,id_temp);
		if(More(temp2,t_max))t_max=temp2,strcpy(id_max,id_temp);
	}
	printf("%s %s\n",id_min,id_max);
	return 0;
}
