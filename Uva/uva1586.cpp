#include<cstdio>
const int M=150;
double s[M];
char c,last;
int main(){
	freopen("UVa1586.txt","r",stdin);
	freopen("ans.txt","w",stdout);

	s['C']=12.01,s['H']=1.008,s['O']=16.00,s['N']=14.01;
	int n;
	scanf("%d\n",&n);
	while(n--){
		double sum=0.0,m=0;
		bool flag=false;
		do{
			c=getchar();
			if(c>='0'&&c<='9'){
				m=m*10+(c-'0'),flag=false;
				
			}
			else if(c>'A'&&c<'Z'){
				if(flag)sum+=s[last];
				else sum+=s[last]*m,m=0;
				last=c;flag=true;
			}
			else{
				if(flag)m=1;
				sum+=s[last]*m;
			}
		}while(c!=EOF&&c!='\n');
		printf("%.3lf\n", sum);
	}
	
	return 0;	
	
}