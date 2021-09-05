class Solution {
public:
    int minFlips(string s) {
        int len = s.size();
        string target = "01";

        int cnt = 0;
        for (int i = 0; i < len; i++) {
            cnt += (s[i] != target[i % 2]);
        }

        s += s;
        int ans = min({ cnt, len - cnt });
        for (int i = 0; i < len; i++) {
            cnt -= (s[i] != target[i % 2]);
            cnt += (s[i + len] != target[(i + len) % 2]);
            ans = min({ ans, cnt, len - cnt });
        }

        return ans;
    }
};


// 作者：ikaruga
// 链接：https://leetcode-cn.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/solution/minimum-number-of-flips-by-ikaruga-lu32/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution {
public:
    int minFlips(string s) {
        auto left = helper(s);
        reverse(s.begin(), s.end());
        auto right = helper(s);
        reverse(right.begin(), right.end());
        int n = s.size();
        int res = min(left.back(),n-left.back());
        for (int i = 1; i < n; i++){
            res = min(res, left[i-1]+n-i-right[i]);
            res = min(res, i-left[i-1]+right[i]);
        }
        return res;
    }
    vector<int> helper(string s){
        int n = s.size(), cur = 0;
        vector<int> dp(n,0);
        for (int i = 0; i < n; i++){
            int val = s[i]-'0';
            cur += (i&1)^val;
            dp[i] = cur;
        }
        return dp;
    }
};