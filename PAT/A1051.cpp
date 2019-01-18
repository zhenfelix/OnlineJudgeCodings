#include<cstdio>
#include<stack>
#include<vector>
using namespace std;
int main(){
	freopen("A1051.txt","r",stdin);
	int m,n,k;
	vector<int>a;
	stack<int>st;
	scanf("%d%d%d",&m,&n,&k);
	while(k--){
		int temp,current=0;
		bool flag=true;
		a.clear();
		while(!st.empty())st.pop();
		for(int i=0;i<n;i++)scanf("%d",&temp),a.push_back(temp);
		for(int i=1;i<=n;i++){
			st.push(i);
			if(st.size()>m){
				flag=false;
				break;
			}
			while(st.size()>0&&st.top()==a[current]){
				printf("%d ",st.top());
				st.pop();
				current++;
			}
		}
		if(st.empty()&&flag)printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
