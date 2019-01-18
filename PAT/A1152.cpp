#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>
using namespace std;
bool isPrime(int num)
{
	if(num<2)	return false;
	for(int i=2;i<=sqrt(num);i++){
		if(num%i==0)	return false;
	}
	return true;
}
int main()
{
//	freopen("1152.txt","r",stdin);
	int n,k;
	string str;
	cin>>n>>k>>str;
	int flag=0;
	for(int i=0;i<str.length()-k+1;i++){    
		string tmp=str.substr(i,k);    //取出长度为K的子串
		int num=stoi(tmp);            //转化为int类型判断是否是素数
		if(isPrime(num)){
			cout<<tmp;
			return 0;                //第一次找到直接输出，并return 0
		}
	}
	cout<<"404";                    //未找到输出“404”
	return 0;	
} 

auto __=[](){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return nullptr;
}();