#include <vector>
#include <string>
#include <stack>
#include <map>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<int> st;
        map<char,int> table;
        string mark="{[( )]}";
        for(int i=0;i<mark.size();i++)table[mark[i]]=i-3;
        for(int i=0;i<s.size();i++){
            int tmp=table[s[i]];
            if(!st.empty()&&tmp>0&&st.top()==-tmp)st.pop();
            else st.push(tmp);
        }
        if(st.size()==0)return true;
        else return false;
    }
};
