#include<cstdio>
#include<vector>
#include<algorithm>
#define N 26*26*26*10+1
using namespace std;
int getID(char s[]){
	int ans=0;
	for(int i=0;i<3;i++){
		ans=ans*26+s[i]-'A';
	}
	ans=ans*10+s[3]-'0';
	return ans;
}
vector<int>stu[N];
int main(){
	freopen("A1039.txt","r",stdin);
	int n,k,course,num;
	scanf("%d%d",&n,&k);
	
	for(int i=0;i<k;i++){
		scanf("%d%d",&course,&num);
		for(int j=0;j<num;j++){
			char s[5];
			scanf("%s",s);
			//printf("%s %d\n",s,j);
			stu[getID(s)].push_back(course);
		}
	}
	char temp[5];
	
	while(scanf("%s",temp)!=EOF){
		int id=getID(temp);
		printf("%s %d",temp,stu[id].size());
		sort(stu[id].begin(),stu[id].end());
		for(int i=0;i<stu[id].size();i++)printf(" %d",stu[getID(temp)][i]);
		printf("\n");
	}
	return 0;
}
