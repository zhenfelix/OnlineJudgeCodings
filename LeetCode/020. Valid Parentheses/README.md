```c++
class Solution {
public:
    bool isValid(string s) {
        stack<int> st;
        map<char,int> table;
        string mark="{[( )]}";
        for(int i=0;i<mark.size();i++)table[mark[i]]=i-3;
        for(int i=0;i<s.size();i++){
            int tmp=table[s[i]];
            if(!st.empty()&&tmp>0&&st.top()==-tmp)st.pop();//determine stack is_empty before stack.top() or stack.pop()
            else st.push(tmp);
        }
        if(st.size()==0)return true;
        else return false;
    }
};

```
