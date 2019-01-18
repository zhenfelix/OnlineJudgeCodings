#include<cstdio>
#include<string>
#include<iostream>
#include<map>
#include<set>
using namespace std;
set<char> mark;
map<string,int> dic;
void init(){
	for(char c='a';c<='z';c++)mark.insert(c);
	for(char c='A';c<='Z';c++)mark.insert(c);
	for(char c='0';c<='9';c++)mark.insert(c);
}
int main(){
	freopen("A1071.txt","r",stdin);
	init();
	char c;
	string temp;
	bool flag=false,next=false;
	while(1){
		if(scanf("%c",&c)==EOF)next=true;
		if(mark.find(c)!=mark.end()&&!next){
			if(c>='A'&&c<='Z')c=c-'A'+'a';
			temp+=c;
			flag=true;
		}
		else if(flag){
			if(dic.find(temp)!=dic.end())dic[temp]++;
			else dic[temp]=1;
			temp.clear();
			flag=false;
		}
		if(next)break;
	}
	int mm=0;
	temp=dic.begin()->first;
	for(map<string,int>::iterator it=dic.begin();it!=dic.end();it++){
		if(it->second>mm)temp=it->first,mm=it->second;
		else if(it->second==mm&&it->first<temp)temp=it->first;
	}
	cout<<temp<<" "<<mm<<endl;
	return 0;
}
