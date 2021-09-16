class Solution {
public:
    int maxUniqueSplit(string s) {
        unordered_set<string> visited;
        int n = s.length();
        function<int(int)> dfs = [&](int cur){
            if (cur == n)
                return 0;
            int res = -1;
            for (int nxt = cur+1; nxt <= n; nxt++){
                string word = s.substr(cur,nxt-cur);
                if (1+n-nxt <= res)
                    break;
                if (visited.count(word) == 0){
                    visited.insert(word);
                    int res_ = dfs(nxt);
                    if (res_ > -1)
                        res = max(res, 1+res_);
                    visited.erase(word);
                }
            }
            return res;
        };
        return dfs(0);
    }
};