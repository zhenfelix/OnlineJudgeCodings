#include<cstdio>
#include<iostream>
#include<string>
#include<map>
using namespace std;
#define log cout<<num<<endl
string unit[13]={"tret", "jan", "feb", "mar", "apr", "may", "jun","jly", "aug", "sep", "oct", "nov", "dec"};
string ten[13]={"tret", "tam", "hel", "maa", "huh", "tou", "kes","hei", "elo", "syy", "lok", "mer", "jou"};
string num2str[170];
map<string,int> str2num;
void init(){
	string str;
	for(int i=0;i<13;i++){
		for(int j=0;j<13;j++){
			if(i==0)num2str[j]=unit[j],str2num[num2str[j]]=j;
			else if(j==0)num2str[i*13]=ten[i],str2num[num2str[i*13]]=i*13;
			else num2str[i*13+j]=ten[i]+" "+unit[j],str2num[num2str[i*13+j]]=i*13+j;
		}
	}
}
int main(){
	freopen("A1100.txt","r",stdin);
	init();
	int n;
	string temp;
	scanf("%d\n",&n);
	while(n--){
		getline(cin,temp);
		if(temp[0]>='0'&&temp[0]<='9'){
			int num=0;
			for(int i=0;i<temp.size();i++){
				num=num*10+temp[i]-'0';
			}
			cout<<num2str[num]<<endl;
		}
		else cout<<str2num[temp]<<endl;
	}
	return 0;
}
