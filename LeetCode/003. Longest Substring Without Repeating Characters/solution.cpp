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


class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> cnt(256, 0);
        int n = s.length();
        int left = 0, res = 0;
        for (int right = 0; right < n; right++){
            cnt[s[right]]++;
            while (cnt[s[right]] > 1)
                cnt[s[left++]]--;
            res = max(res, right-left+1);
        }
        return res;
    }
};
