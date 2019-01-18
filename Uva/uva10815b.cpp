#include<cstdio>
#include<iostream>
#include<string>
#include<ctype>
#include<set>
set<string> dict;

int main(){
	freopen("uva10815.txt","r",stdin);
	freopne("ans.txt","w",stdout);
	string buff;
	char ch;
	while((ch=getchar())!=EOF){
		if(isalpha(ch))buff+=ch;
		else{
			dict.insert(buff);
			buff.clear();
		}
	}
	for(set<string>::iterator it=dict.begin();it!=dict.end();it++)cout<<*it<<"\n";
	return 0;
}