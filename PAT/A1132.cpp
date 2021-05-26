// #include<cstdio>
// #include<algorithm>
// #include<cstring>
// using namespace std;
// const int nmax=25;
// char str[nmax];

// long long str2int(int xyz[],int len){
// 	long long sum=0;
// 	for(int i=0;i<len;i++){
// 		sum=sum*10+xyz[i];
// 	}
// 	return sum;
// }
// void read_data(){
// 	int n,nh;
// 	int x[nmax],a[nmax],b[nmax];
// 	bool flag=false;
// 	gets(str);
// 	n=strlen(str);nh=n/2;
// 	for(int i=0;i<n;i++)x[i]=str[i]-'0';
// 	for(int i=0;i<nh;i++)a[i]=str[i]-'0';
// 	for(int i=nh;i<n;i++)b[i-nh]=str[i]-'0';
// 	long long temp=(str2int(b,nh)*str2int(a,nh));
// 	long long t=str2int(x,n);
// 	if(temp==0)flag=false;
// 	else if(t%temp==0)flag=true;
// 	if(flag)printf("Yes\n");
// 	else printf("No\n");
// 	return;
// }
// int main(){
// 	//freopen("a.txt","r",stdin);
// 	int num;
// 	scanf("%d\n",&num);
// 	for(int i=0;i<num;i++){
// 		read_data();
// 	}
// 	return 0;
// }



#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");
const int inf = 0x3f3f3f3f;

int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
//     freopen("input", "r", stdin);
    int n;
    cin >> n;
    string num;
    for (int i = 1; i <= n; i++){
        cin >> num;
        int len = num.size();
        int half = len/2;
        int numerator = std::stoi(num);
        int denominator = std::stoi(num.substr(0, half)) * std::stoi(num.substr(half));
        if (denominator > 0 && numerator % denominator == 0)
            cout << "Yes\n";
        else 
            cout << "No\n";
    }
    
    return 0;
}
