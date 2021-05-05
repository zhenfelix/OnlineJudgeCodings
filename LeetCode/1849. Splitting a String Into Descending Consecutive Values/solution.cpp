using LL = long long;

class Solution {
public:
    bool dfs(string &s, LL pre, int i){
        if (i == s.size())
            return true;
        LL cur = 0;
        while (i < s.size()){
            cur *= 10;
            cur += s[i++]-'0';
            if (cur == pre-1 && dfs(s, cur, i))
                return true;
            if (cur > pre-1)
                return false;
        }
        return false;
    }

    bool splitString(string s) {
        LL cur = 0;
        for (int i = 0; i+1 < s.size();){
            cur *= 10;
            cur += s[i++]-'0';
            if (cur > (LL) INT_MAX*10)
                break;
            if (dfs(s, cur, i))
                return true;
        }
        return false;
    }
};