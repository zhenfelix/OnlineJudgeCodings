class Solution {
public:
    int longestBeautifulSubstring(string word) {
        const auto n = word.size();

        int cnt = 1;
        int len = 1;
        int max_len = 0;
        for (int i = 1; i != n; ++i) {
            if (word[i - 1] == word[i]) {
                ++len;
            } else if (word[i - 1] < word[i]) {
                ++len;
                ++cnt;
            } else {
                cnt = 1;
                len = 1;
            }
            
            if (cnt == 5) {
                max_len = max(max_len, len);
            }
        }
        return max_len;
    }
};



class Solution {
public:
    int longestBeautifulSubstring(string word) {
        std::vector<int> mp(128);
        string s = "aeiou";
        for (int i = 0; i < 5; i++){
            mp[s[i]] = i;
        }
        int dp = 5, pre, res = 0, sz;
        for (auto ch : word){
            int cur = mp[ch];
            if (dp < 5 && (cur == pre || cur == pre+1)){
                dp = cur;
                sz++;
                if (dp == 4)
                    res = max(res, sz);
            }
            else{
                dp = 5;
                if (cur == 0){
                    dp = 0;
                    sz = 1;
                }
            }
            pre = cur;
            // cout << cur << " " << dp << " " << sz << endl;

        }
        return res;
    }
};

