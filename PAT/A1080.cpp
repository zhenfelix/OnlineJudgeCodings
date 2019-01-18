#include<cstdio>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;
#define maxn 40010
#define maxm 110
int n,m,k;
struct student{
	int idx,ge,gi,ga,rank,app[5];
}stu[maxn];
int school[maxm];
queue<int> q,qt;
int result[maxm][maxn];
int Count[maxm]={0};
bool Hashtable[maxm]={false};
bool cmp(student a,student b){
	if(a.ga!=b.ga)return a.ga>b.ga;
	else return a.ge>b.ge;
}
void admit(int x){
	for(int i=0;i<k;i++){
		int temp=stu[x].app[i];
		if(school[temp]>0||Hashtable[temp]){
			result[temp][Count[temp]++]=(stu[x].idx);
			Hashtable[temp]=true;
			qt.push(temp);
			school[temp]--;
			break;
		}
	}
}
int main(){
	freopen("A1080.txt","r",stdin);
	scanf("%d%d%d",&n,&m,&k);
	for(int i=0;i<m;i++)scanf("%d",&school[i]);
	for(int i=0;i<n;i++){
		stu[i].idx=i;
		scanf("%d%d",&stu[i].ge,&stu[i].gi);
		stu[i].ga=stu[i].ge+stu[i].gi;
		for(int j=0;j<k;j++)scanf("%d",&stu[i].app[j]);
	}
	sort(stu,stu+n,cmp);
	stu[0].rank=0;
	q.push(0);
	for(int i=1;i<=n;i++){
		if(stu[i].ga==stu[i-1].ga&&stu[i].ge==stu[i-1].ge&&i<n){
			stu[i].rank=stu[i-1].rank;
			q.push(i);
		}
		else{
			while(!q.empty()){
				int temp=q.front();
				admit(temp);
				q.pop();
			}
			while(!qt.empty()){
				int temp=qt.front();
				Hashtable[temp]=false;
				qt.pop();
			}
			stu[i].rank=i;
			q.push(i);
		}
	}
	for(int i=0;i<m;i++){
		int temp=Count[i];
		if(temp>0)sort(result[i],result[i]+temp);
		for(int j=0;j<temp;j++){
			printf("%d",result[i][j]);
			if(j<temp-1)printf(" ");
		}
		printf("\n");
	}
}
