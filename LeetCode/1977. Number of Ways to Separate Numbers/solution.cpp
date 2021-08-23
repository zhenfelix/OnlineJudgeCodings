using ll = long long;
const ll MOD = 1e9 + 7;

class Solution {
public:
    int numberOfCombinations(string num) {
        if (num[0] == '0')
            return 0;
        
        int n = num.size();
        vector<vector<ll>> dp(n + 1, vector<ll>(n + 1));
        dp[1] = vector<ll>(n + 1, 1);
        dp[1][0] = 0;
        
        vector<vector<int>> c(n, vector<int>(n));
        for (int len = 1; len <= n; ++len)
            for (int i = n - 1 - len; i >= 0; --i) {
                if (num[i] < num[i + len])
                    c[i][i + len] = n - i - len;
                else if (num[i] == num[i + len]) {
                    if (i + len == n - 1)
                        c[i][i + len] = 1;
                    else
                        c[i][i + len] = c[i + 1][i + len + 1] + 1;
                }
            }
        
        auto cmp = [&](int l, int r, int len) {
            if (l < 0)
                // return false; both ok
                return true;
            return c[l][r] >= len;
        };
        
        for (int i = 2; i <= n; ++i) {
            dp[i][i] = 1;
            for (int j = 1; j < i; ++j) {
                if (num[i - j] == '0')
                    continue;
                if (cmp(i - 2 * j, i - j, j))
                    dp[i][j] = (dp[i][j] + dp[i - j][j]) % MOD;
                else
                    dp[i][j] = (dp[i][j] + dp[i - j][j - 1]) % MOD;   
            }
            for (int j = 1; j <= n; ++j)
                dp[i][j] = (dp[i][j] + dp[i][j - 1]) % MOD;
        }
        
        return dp[n][n];
    }
};


作者：lucifer1004
链接：https://leetcode-cn.com/problems/number-of-ways-to-separate-numbers/solution/liang-ci-dong-tai-gui-hua-qian-zhui-he-b-r29b/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。