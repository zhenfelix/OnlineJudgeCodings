#include<iostream>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <algorithm>
#include <cctype>
using namespace std;

vector<vector<string> > docs;
typedef pair<int, int> pii;
typedef vector<pii> did;
map<string,did> dic;
int num_doc=0,num_line=0;



void end_doc(){
    for(int i=0;i<10;i++)cout<<"-";
    cout<<endl;
    return;
}
void end_query(){
    for(int i=0;i<10;i++)cout<<"=";
    cout<<endl;
    return;
}

void lower_case(string &str){
    for(int i=0;i<str.size();i++){
        if(str[i]>='A'&&str[i]<='Z')str[i]=str[i]-'A'+'a';
    }
    return;
}
void parse(string str){
    lower_case(str);
    str+=" ";
    string tmp;
    char ch;
    for(int i=0;i<str.size();i++) {
        ch=str[i];
        if(isalpha(ch))tmp+=ch;
        else{
            pii x(num_doc,num_line);
            if(!dic.count(tmp)){
                did entry;
                entry.push_back(x);
                dic[tmp]=entry;
            }
            else{
                did pre=dic[tmp];
                dic[tmp].push_back(x);
            }
            tmp.clear();
        }
    }
    return;
}
void print_query(did ans){
    int x=0,y,tmp,len;
    pii z;
    bool flag=false;
    len=ans.size();
    if(len==0){
        cout<<"Sorry, I found nothing."<<endl;
    }
    else{
        for(int i=0;i<len;i++){
            if(i==len-1||ans[i]!=ans[i+1]){//skip repeated queried lines
                z=ans[i];
                tmp=z.first;y=z.second;
                if(tmp!=x&&flag)end_doc();
                x=tmp;
                flag=true;
                cout<<docs[x][y]<<endl;
            }
        }
    }
    end_query();
    return;
}

bool query(string str,did &ans){
    lower_case(str);
    if(!dic.count(str))return false;
    else ans=dic[str];
    return true;
}


int main() {
//    freopen("uva1597.txt", "r", stdin);
//    freopen("ans.txt", "w", stdout);
    int n;
    scanf("%d\n",&n);
    while(n--){
        string line;
        vector<string> doc;
        num_line=0;
        while(getline(cin, line),line.substr(0,1)!="*"){
            //            doc.push_back(line);
            parse(line);
            doc.push_back(line);
            num_line++;
        }
        docs.push_back(doc);
        num_doc++;
    }
    scanf("%d\n",&n);
    while (n--) {
        string line,tmp;
        vector<string> q;
        did ans1,ans2,ans;
        getline(cin,line);
        stringstream ss(line);
        while(ss>>tmp)q.push_back(tmp);
        if(q.size()==1){
            query(q[0], ans1);
            ans=ans1;
        }
        else if(q.size()==2){
            query(q[1], ans1);
            int len=docs.size();
            set<int> exist_doc;
            for(int i=0;i<ans1.size();i++)if(!exist_doc.count(ans1[i].first))exist_doc.insert(ans1[i].first);
            for(int i=0;i<len;i++){
                if(!exist_doc.count(i))for(int j=0;j<docs[i].size();j++){
                    pii x(i,j);
                    ans.push_back(x);
                }
            }
        }
        else{
            query(q[0], ans1);query(q[2], ans2);
            set<int> exist_doc1,exist_doc2,exist_doc;
            for(int i=0;i<ans1.size();i++)if(!exist_doc1.count(ans1[i].first))exist_doc1.insert(ans1[i].first);
            for(int i=0;i<ans2.size();i++)if(!exist_doc2.count(ans2[i].first))exist_doc2.insert(ans2[i].first);
            if(q[1][0]=='A')set_intersection(exist_doc1.begin(), exist_doc1.end(), exist_doc2.begin(), exist_doc2.end(),inserter(exist_doc, exist_doc.begin()));
            else set_union(exist_doc1.begin(), exist_doc1.end(), exist_doc2.begin(), exist_doc2.end(),inserter(exist_doc, exist_doc.begin()));
            for(int i=0;i<ans1.size();i++)if(exist_doc.count(ans1[i].first))ans.push_back(ans1[i]);
            for(int i=0;i<ans2.size();i++)if(exist_doc.count(ans2[i].first))ans.push_back(ans2[i]);
            sort(ans.begin(), ans.end());
        }
        print_query(ans);
        q.clear();
        
    }
    //        for(int i=0;i<docs.size();i++){
    //            for(int j=0;j<docs[i].size();j++){
    //                cout<<docs[i][j]<<endl;
    //            }
    //            end_doc();
    //        }
    
    return 0;
}


