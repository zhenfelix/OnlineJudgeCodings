#include <iostream>
#include<cstring>
#include<cmath>
#include<set>
using namespace std;
set<int> is_mod;
char str[100000];
int a,b;
int main() {
    freopen("input.txt", "r", stdin);
    scanf("%d%d%s",&a,&b,str);
    int t,k=-1,i=0,j=0,cc=0;
    bool flag=false,temp=false;
    a=a%b;
    while(!flag&&cc<strlen(str)){
        if(is_mod.count(a))cc++;
        is_mod.insert(a);
        a=a*10;
        t=a/b;
        a=a%b;
        i++;
        if(t==str[j]-'0'){
            if(!temp){temp=true;j++;k=i;}
            else{
                j++;
                if(j>=strlen(str)){
                    flag=true;
                    break;
                }
            }
        }
        else{
            temp=false;j=0;k=-1;
        }
    }
    if(!flag)k=-1;
    printf("%d",k);
    return 0;
}
