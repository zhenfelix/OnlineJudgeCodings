#include<cstdio>
int map(char p)
{
	if(p=='B')return 0;
	else if(p=='C')return 1;
	else return 2;
}
int main()
{
	int w=0,f=0,m,a[3]={0},b[3]={0},n,temp1=0,temp2=0,index1=0,index2=0;
	char A,B,mp[3]={'B','C','J'};
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		getchar();
		scanf("%c %c",&A,&B);
		if((map(A)+1)%3==map(B))w++,a[map(A)]++;
		else if((map(B)+1)%3==map(A))f++,b[map(B)]++;
	}
	m=n-f-w;
	printf("%d %d %d\n",w,m,f);
	printf("%d %d %d\n",f,m,w);
	for(int i=0;i<3;i++){
		if(temp1>a[i])temp1=a[i],index1=i;
		if(temp2>b[i])temp2=b[i],index2=i;
	}
	printf("%c %c\n",mp[index1],mp[index2]);
	return 0;
}
