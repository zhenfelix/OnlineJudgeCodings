#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstring>
using namespace std;
const int maxn=40010;
const int maxk=2510;
char name[maxn][5];
vector<int> course[maxk];
bool cmp(int a,int b){
	return strcmp(name[a],name[b])<0;
}
int main(){
	freopen("A1047.txt","r",stdin);
	int n,k,num;
	char temp[5];
	scanf("%d%d",&n,&k);
	for(int i=0;i<n;i++){
		scanf("%s%d",temp,&num);
		strcpy(name[i],temp);
		for(int j=0;j<num;j++){
			int c;
			scanf("%d",&c);
			course[c].push_back(i);
		}
	}
	for(int i=1;i<=k;i++){
		printf("%d %d\n",i,course[i].size());
		sort(course[i].begin(),course[i].end(),cmp);
		for(int j=0;j<course[i].size();j++)printf("%s\n",name[course[i][j]]);
	}
	return 0;
}
