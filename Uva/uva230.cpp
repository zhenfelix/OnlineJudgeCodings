#include<iostream>
#include <vector>
#include <map>
#include <sstream>
#include <algorithm>
using namespace std;
string end_mark="E",quo_mark="\"",b_mark="B",r_mark="R",s_mark="S";
void parse(string line,string &a,string &b){
    stringstream ss(line);
    string x;
    bool flag_a=false,flag_b=true;
    while (ss>>x){
        //        cout<<x<<endl;
        if(x.substr(0,1)==quo_mark)flag_a=!flag_a,flag_b=!flag_b;
        x+=" ";
        if(flag_a)a+=x;
        if(flag_b)b+=x;
        if(x.substr(x.size()-2,1)==quo_mark)flag_a=!flag_a,flag_b=!flag_b;
        
        //        if(flag_flip)flag_a=!flag_a,flag_b=!flag_b,flag_flip=!flag_flip;
    }
    if(a.size()>0)a=a.substr(1,a.size()-3);
    return;
}
struct Book{
    string title,author;
    int state=0;
};
bool cmp(Book a,Book b){
    if(a.author!=b.author)return a.author<b.author;
    else return a.title<b.title;
}
vector<Book>books;
vector<int>r;
map<string,int>dic;
void print(){
    sort(r.begin(), r.end());
    for(int i=0;i<r.size();i++){
        if(i>0&&r[i]==r[i-1]){
            books[r[i]].state++;
            continue;
        }
        cout<<"Put \""<<books[r[i]].title<<"\" ";
        books[r[i]].state++;
        int j=r[i]-1;
        for(;j>=0;j--)if(books[j].state)break;
        if(j>=0)cout<<"after \""<<books[j].title<<"\""<<endl;
        else cout<<"first"<<endl;
    }
}

int main() {
//    freopen("uva230.txt", "r", stdin);
//    freopen("ans.txt", "w", stdout);
    string line;
    while(getline(cin, line),line.substr(0,1)!=end_mark){
        string title,author;
        parse(line, title, author);
        author=author.substr(3,author.size()-4);
        if(dic.count(title))books[dic[title]].state++;
        else{
            Book temp;
            temp.title=title;temp.author=author;temp.state=1;
            books.push_back(temp);
        }
        
        
        
        //        cout<<title<<"-"<<author<<"-"<<endl;
    }
    sort(books.begin(),books.end(),cmp);
    for(int i=0;i<books.size();i++)dic[books[i].title]=i;
    while(getline(cin, line),line.substr(0,1)!=end_mark){
        string cmd,query;
        parse(line, query, cmd);
        cmd=cmd.substr(0,cmd.size()-1);
        if(cmd.substr(0,1)==b_mark)books[dic[query]].state--;
        if(cmd.substr(0,1)==r_mark)r.push_back(dic[query]);
        if(cmd.substr(0,1)==s_mark){
            print();
            cout<<"END"<<endl;
            r.clear();
        }
        //        cout<<cmd<<"-"<<query<<"-"<<endl;
    }
    return 0;
    
}


