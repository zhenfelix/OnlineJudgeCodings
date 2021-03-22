class Solution {
public:
    int longestPalindrome(string s) {
        vector<int> cnt(256,0);
        for(auto ch: s)cnt[ch] += 1;
        int odd = 0, res = 0;
        for(auto x: cnt){
            if(x&1) odd = 1;
            res += x/2*2;
        }
        return res + odd;
    }
};