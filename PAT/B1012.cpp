#include<cstdio>
int main()
{
	int ans[5]={0},count[5]={0},i,x,n;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&x);
		if(x%5==0){
			if(x%10==0){
				ans[0]+=x;
				count[0]++;
			}
		}
		else if(x%5==1){
			if(count[1]%2==0)ans[1]+=x;
			else ans[1]-=x;
			count[1]++;
		}
		else if(x%5==2){
			count[2]++;
			ans[2]=count[2];
		}
		else if(x%5==3){
			ans[3]+=x;
			count[3]++;
		}
		else{
			if(x>ans[4])ans[4]=x;
			count[4]++;
		}
	}
	for(i=0;i<5;i++)
	{
		if(count[i]==0)printf("%c",'N');
		else if(i==3)printf("%.1f",ans[3]*1.0/count[3]);
		else printf("%d",ans[i]);
		if(i<4)printf(" ");
	}
}
