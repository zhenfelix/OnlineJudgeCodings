class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int dp = 0, res = 0, n = s.length();
        vector<int> last(256,-1);
        for(int i=0;i<n;i++){
            int ch = s[i];
            dp = max(dp, last[ch]+1);
            res = max(res, i-dp+1);
            last[ch] = i;
        }
        return res;
    }
};