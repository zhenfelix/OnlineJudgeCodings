#include<cstdio>
#include<cstring>

int main(){
	freopen("B1024.txt","r",stdin);
	char num[10000],sym1,sym2,e[10];
	int i,j,count1=0,count2=0,len,pow=0;
	gets(num);
	len=strlen(num);
	i=1;
	while(num[i++]!='E')count1++;
	sym1=num[0],sym2=num[count1+2];
	i=count1+3,j=0;
	while(num[i]!='\0'){
		e[j++]=num[i],count2++;
		i++;
	}
	for(i=0;i<count2;i++){
		pow*=10;
		pow+=(e[i]-'0');
	}
	if(sym1=='-')printf("%c",sym1);
	if(sym2=='+'){
		printf("%c",num[1]);
		if(pow>=count1-2){
			for(i=3;i<=count1;i++)printf("%c",num[i]);
			for(i=0;i<(pow-count1+2);i++)printf("%c",'0');
		}
		else{
			for(i=3;i<=(pow+2);i++)printf("%c",num[i]);
			printf(".");
			for(i=(pow+3);i<=count1;i++)printf("%c",num[i]);
		}
	}
	else{
		if(pow==0)for(i=1;i<=count1;i++)printf("%c",num[i]);
		else{
			printf("0.");
		    for(i=1;i<pow;i++)printf("0");
	     	printf("%c",num[1]);
	    	for(i=3;i<=count1;i++)printf("%c",num[i]);
		}
		
	}
	return 0;
}
