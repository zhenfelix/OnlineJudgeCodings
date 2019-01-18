#include<iostream>
#include <vector>
#include <map>
#include <sstream>
#include <algorithm>
using namespace std;

const int maxn=150;
struct Array{
    int size;
    map<int,int> id2v;
};
Array a[maxn];

bool is_assign(string line,int &k){
    int i;
    for(i=0;i<line.size();i++)if(line.substr(i,1)=="=")break;
    k=i;
    if(k<line.size())return true;
    return false;
}
int str2int(string str){
    int sum=0;
    for(int i=0;i<str.size();i++){
        sum=sum*10+str[i]-'0';
    }
    return sum;
}
void check(string str,bool &error,int &val){
    if(str[0]>='0'&&str[0]<='9'){
        val=str2int(str.substr(0,str.size()));
    }
    else{
        check(str.substr(2,str.size()-3), error, val);
        if(error);
        else if(!a[str[0]].id2v.count(val))error=true;
        else{
            val=a[str[0]].id2v[val];
        }
    }
}
int main() {
//    freopen("uva1596.txt", "r", stdin);
//    freopen("ans.txt", "w", stdout);
    string line;
    int line_num=-1;
    while(1){
        if(line_num==0)break;
        line_num=0;
        for(int i=0;i<maxn;i++){
            a[i].size=0;
            a[i].id2v.clear();
        }
        bool error=false;
        while(getline(cin, line),line!="."){
            int k;
            if(error)continue;
            if(!is_assign(line, k)){
                char name=line[0];
                a[name].size=str2int(line.substr(2,line.size()-3));
//                if(a[name].size<1)error=true;
//                else error=true;
//                cout<<a[name].size<<endl;
            }
            else{
                bool flag1=false,flag2=false,flag3=false;
                int val1,val2;
                check(line.substr(2,k-3), flag1, val1);
                check(line.substr(k+1), flag2, val2);
                if(a[line[0]].size<=val1)flag3=true;
                a[line[0]].id2v[val1]=val2;
                error=flag3||flag2||flag1;
            }
//            cout<<is_assign(line, k)<<" "<<k<<endl;
            line_num++;
            if(error)cout<<line_num<<endl;
        }
        if(!error&&line_num)cout<<0<<endl;
    }
    return 0;
}


