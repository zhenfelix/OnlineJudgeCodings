#include<cstdio>
#include<string>
#include<iostream>
using namespace std;
int n;
string chop(string a,int &t){
	string b;
	int count=0;
	bool flag=false;
	while(a[0]=='0')a.erase(a.begin());
	if(a[0]=='.'){
		a.erase(a.begin());
		flag=true;
		while(a[0]=='0'){
			a.erase(a.begin());
			t--;
		}
	}
	if(a.size()==0)t=0;
	for(int i=0;i<a.size();i++){ 
		if(a[i]=='.')flag=true;
		else{
			if(count>=n){
				if(flag)break;
				else t++;
			}
			else{
				if(flag);
				else t++;
				b+=a[i];
				count++;
			}
		}
	}
	while(count<n){
		b+='0';
		count++;
	}
	b.insert(0,"0.");
	b+="*10^";
	return b;
}
int main(){
	freopen("A1060.txt","r",stdin);
	int T=2;
	while(T--){
	string x,y,ans1,ans2;
	int t1=0,t2=0;
	cin>>n>>x>>y;
	ans1=chop(x,t1);
	ans2=chop(y,t2);
	if(ans1==ans2&&t1==t2)cout<<"YES "<<ans1<<t1<<endl;
	else cout<<"NO "<<ans1<<t1<<" "<<ans2<<t2<<endl;
	}
	return 0;
}
