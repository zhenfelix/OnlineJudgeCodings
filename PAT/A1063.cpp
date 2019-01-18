#include<cstdio>
#include<set>
using namespace std;
const int N=55;
set<int> st[N];
void similar(int a,int b){
	
	int t_num=st[b].size(),p_num=0;
	for(set<int>::iterator it=st[a].begin();it!=st[a].end();it++){
		if(st[b].find(*it)!=st[b].end())p_num++;
		else t_num++;
	}
	printf("%.1f\%\n",p_num*100.0/t_num);
}
int main(){
	freopen("A1063.txt","r",stdin);
	int n,num,temp,m,a,b;
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		scanf("%d",&num);
		for(int j=0;j<num;j++){
			scanf("%d",&temp);
			st[i].insert(temp);
		}
	}
	scanf("%d",&m);
	for(int i=0;i<m;i++){
		scanf("%d%d",&a,&b);
		similar(a,b);
	}
	return 0;
}
