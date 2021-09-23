class Solution {
    int k;
    unordered_map<char, int> cnt;
    string s, t, ans;
    
    void dfs() {
        unordered_map<char, int> cnt2(cnt);
        for (auto [ch, freq] : cnt2) {
            t.push_back(ch);
            if (t.size() > ans.size() || (t.size() == ans.size() && t > ans)) {
                int times = 0, pos = 0;
                for (char c : s)
                    if (c == t[pos]) {
                        pos++;
                        if (pos == t.size())
                            times++, pos = 0;
                    }

                if (times >= k)
                    ans = t;
            }
            cnt[ch] -= k;
            if (cnt[ch] < k)
                cnt.erase(ch);
            dfs();
            t.pop_back();
            cnt[ch] = freq;
        }
    }
public:
    string longestSubsequenceRepeatedK(string s, int k) {
        this->k = k;
        int n = s.size();
        for (char c : s)
            cnt[c]++;
        string to_del;
        for (auto [ch, freq] : cnt)
            if (freq < k)
                to_del.push_back(ch);
        for (char ch : to_del)
            cnt.erase(ch);
        
        for (char c : s)
            if (cnt.count(c))
                this->s.push_back(c);
        
        dfs();
        
        return ans;
    }
};


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/pmjXoM/view/BaQBMq/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。