#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
struct people{
	char name[10];
	int age,worth;
}r[100010];
bool cmp(people a,people b){
	if(a.worth!=b.worth)return a.worth>b.worth;
	else if(a.age!=b.age)return a.age<b.age;
	else return strcmp(a.name,b.name)<0;
}
int main(){
	freopen("A1055.txt","r",stdin);
	int n,k,m,left,right,i,j,count;
	scanf("%d%d",&n,&k);
	for(i=0;i<n;i++)scanf("%s %d%d",r[i].name,&r[i].age,&r[i].worth);
	sort(r,r+n,cmp);
	for(i=0;i<k;i++){
		scanf("%d%d%d",&m,&left,&right);
		printf("Case #%d:\n",i+1);
		count=0;
		for(j=0;j<n;j++){
			if(r[j].age<=right&&r[j].age>=left){
				printf("%s %d %d\n",r[j].name,r[j].age,r[j].worth);
				count++;
			}
			if(count>=m)break;
		}
		if(count==0)printf("None\n");
		
	}
	return 0;
}
