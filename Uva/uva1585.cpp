#include<stdio.h>
int main(){
    // freopen("UVa1585.txt","r",stdin);
    int n;
    scanf("%d\n",&n);
    while(n--){
    	char c;
    	int term=0,sum=0;
    	while((c=getchar())!='\n'&&c!=EOF){
    	    if(c=='O')term++;
    	    else term=0;
    	    sum+=term;
    	}
    	printf("%d\n",sum);
    }    
    return 0;
}
