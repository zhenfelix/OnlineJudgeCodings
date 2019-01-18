#include<cstdio>
struct Student{
	char name[15],S,id[15];
	int score;
}ma_low,fe_high,temp;

void init(){
	ma_low.score=101;
	fe_high.score=-1;
}

int main(){
	//freopen("A1036.txt","r",stdin);
	int n,i;
	bool male=false,female=false;
	init();
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%s %c %s %d",temp.name,&temp.S,temp.id,&temp.score);
		if(temp.S=='M'){
			//printf("ok\n");
			if(temp.score<ma_low.score)ma_low=temp,male=true;
		}
		else{
			if(temp.score>fe_high.score)fe_high=temp,female=true;
		}
	}
	if(female==true)printf("%s %s\n",fe_high.name,fe_high.id);
	else printf("Absent\n");
	if(male==true)printf("%s %s\n",ma_low.name,ma_low.id);
	else printf("Absent\n");
	if(female==false||male==false)printf("NA\n");
	else printf("%d\n",fe_high.score-ma_low.score);
	return 0;
}
