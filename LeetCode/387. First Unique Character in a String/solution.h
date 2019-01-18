class Solution {
public:
    int firstUniqChar(string s) {
        map<char,int> st;
        for(int i=0;i<s.size();i++){
            if(st.find(s[i])==st.end())st[s[i]]=1;
            else st[s[i]]++;
        }
        for(int i=0;i<s.size();i++)if(st[s[i]]==1)return i;
        return -1;
    }
};