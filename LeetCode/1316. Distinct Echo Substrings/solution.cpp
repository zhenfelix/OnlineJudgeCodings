class Solution {
public:
    int distinctEchoSubstrings(string text) {
        int n = text.length();
        unordered_set<string> res;
        vector<vector<int>> dp(n, vector<int>(n,0));
        for (int i = n-1; i >= 0; i--){
            for (int j = i+1; j < n; j++){
                if (text[i] != text[j])
                    continue;
                dp[i][j] = 1 + (j+1 < n ? dp[i+1][j+1] : 0);
                if (dp[i][j] >= j-i){
                    res.insert(text.substr(i,j-i));
                    // cout << text.substr(i,j-i) << " " << i << " " << j << " " << j-i << endl;
                }
            }
        }
        return res.size();
    }
};

// class Solution {
// public:
//     int distinctEchoSubstrings(string text) {
//         if (text.size() <= 1) return 0;
//         int N = text.size();
//         // dp[i][j] = k means strcmp (text.data () + i, text.data() + j, k) == 0
//         vector<vector<int>> dp (N + 1, vector<int> (N + 1, 0));
//         unordered_set<string> res;
//         auto &ch = text;
//         for (int j = N-1; j > 0; j--) {
//             for (int i = j-1; i >= 0; i--) {
//                 dp[i][j] = ch[i] == ch[j] ? 1 + dp[i+1][j+1] : 0;
//                 if (dp[i][j] >= j-i) {
//                     res.insert ( ch.substr(i, j-i)); 
//                 }
//             }
//         }
//         return res.size();
//     }
// };


using LL = long long;

class Solution {
private:
    constexpr static int mod = (int)1e9 + 7;
    
public:
    int gethash(const vector<int>& pre, const vector<int>& mul, int l, int r) {
        return (pre[r + 1] - (LL)pre[l] * mul[r - l + 1] % mod + mod) % mod;
    }
    
    int distinctEchoSubstrings(string text) {
        int n = text.size();
        
        int base = 31;
        vector<int> pre(n + 1), mul(n + 1);
        pre[0] = 0;
        mul[0] = 1;
        for (int i = 1; i <= n; ++i) {
            pre[i] = ((LL)pre[i - 1] * base + text[i - 1]) % mod;
            mul[i] = (LL)mul[i - 1] * base % mod;
        }
        
        unordered_set<int> seen;
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int l = j - i;
                if (j + l <= n) {
                    int hash_left = gethash(pre, mul, i, j - 1);
                    if (hash_left == gethash(pre, mul, j, j + l - 1)) {
                        seen.insert(hash_left);
                    }
                }
            }
        }
        return seen.size();
    }
};


// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/distinct-echo-substrings/solution/bu-tong-de-xun-huan-zi-zi-fu-chuan-by-leetcode-sol/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。