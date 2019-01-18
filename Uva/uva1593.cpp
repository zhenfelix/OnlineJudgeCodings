#include<iostream>
#include<string>
#include<sstream>
#include <vector>
using namespace std;

const int maxn=1005;
vector<int>width;
vector<string> str[maxn];
void print(string tmp,int n){
    cout<<tmp;
    for(int i=0;i<n-tmp.size()+1;i++)cout<<" ";
    return;
}
int main() {
//    freopen("uva1593.txt", "r", stdin);
//    freopen("ans.txt", "w", stdout);
    string line;
    int k=0;
    while(getline(cin, line))
    {
        string x;
        stringstream ss(line);
        while(ss>>x){
            str[k].push_back(x);
            if(str[k].size()>width.size())width.push_back(x.size());
            else if(x.size()>width[str[k].size()-1])width[str[k].size()-1]=x.size();
        }
        k++;
    }
//    cout<<k<<endl;
    for(int i=0;i<k;i++){//k be careful of the input file, "\n" could take up a extra line, but not for the standard uva input test case
        int j;
        for(j=0;j<str[i].size()-1;j++)print(str[i][j],width[j]);
        cout<<str[i][j]<<endl;
    }
    return 0;
    
}
