#include<iostream>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <algorithm>
#include <cctype>
using namespace std;

map<string,string>dic_old,dic_new;
set<string>set_add,set_delete,set_change;
string sym="+-*";

void parse(string str,map<string,string> &dic){
    string key,value;
    char ch;
    int len=str.size();
    bool key_flag=false,value_flag=false;
    for(int i=0;i<len;i++){
        ch=str[i];
        if(isalpha(ch))key+=ch,key_flag=true;
        else if(isdigit(ch))value+=ch,value_flag=true;
        else if(key_flag&&value_flag){
            dic[key]=value;
            key.clear();value.clear();
            key_flag=false;value_flag=false;
        }
    }
    return;
}
void print_set(set<string> ss,bool &flag,int choice){
    if(ss.size()>0)flag=true,cout<<sym[choice];
    int i=0;
    for(set<string>::iterator it=ss.begin();it!=ss.end();it++){
        cout<<*it;
        if(i<ss.size()-1)cout<<',';
        else cout<<endl;
        i++;
    }
    return;
}



int main() {
//    freopen("uva12504.txt", "r", stdin);
//    freopen("ans.txt", "w", stdout);
    int n;
    scanf("%d\n",&n);
    while(n--){
        string line;
        getline(cin, line);
        parse(line,dic_old);
        getline(cin,line);
        parse(line,dic_new);
        string key,value;
        for(map<string,string>::iterator it=dic_old.begin();it!=dic_old.end();it++){
            key=it->first,value=it->second;
            if(!dic_new.count(key))set_delete.insert(key);
            else if (value!=dic_new[key])set_change.insert(key);
        }
        for(map<string,string>::iterator it=dic_new.begin();it!=dic_new.end();it++){
            key=it->first;
            if(!dic_old.count(key))set_add.insert(key);
        }
        bool f1=false,f2=false,f3=false;
        print_set(set_add, f1, 0);
        print_set(set_delete, f2, 1);
        print_set(set_change, f3, 2);
        if(!f1&&!f2&&!f3)cout<<"No changes"<<endl;
        cout<<endl;
        dic_new.clear();dic_old.clear();
        set_add.clear();set_delete.clear();set_change.clear();
    }

    
    return 0;
}


