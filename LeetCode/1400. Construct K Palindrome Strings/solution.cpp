class Solution {
public:
    bool canConstruct(string s, int k) {
        int odds = 0, len = s.size();
        vector<int> cnt(26,0);
        for (auto ch : s)
            cnt[ch-'a']++;
        for (int i = 0; i < 26; i++){
            if (cnt[i]&1)
                odds++;
        }
        if (odds > k || len < k)
            return false;
        return true;
    }
};