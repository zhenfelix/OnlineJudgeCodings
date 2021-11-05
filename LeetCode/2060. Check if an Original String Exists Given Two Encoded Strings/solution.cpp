class Solution {
    bool isdigit(char ch) {
        return ch >= '0' && ch <= '9';
    }
public:
    bool possiblyEquals(string s1, string s2) {
        int n = s1.size(), m = s2.size();
        vector<vector<unordered_set<int>>> dp(n + 1, vector<unordered_set<int>>(m + 1));
        dp[0][0].emplace(0);
                
        for (int i = 0; i <= n; ++i) {
            for (int j = 0; j <= m; ++j) {
                for (int delta : dp[i][j]) {
                    int num = 0;
                    for (int p = i; p < min(i + 3, n); ++p) {
                        if (isdigit(s1[p])) {
                            num = num * 10 + s1[p] - '0';
                            dp[p + 1][j].emplace(delta + num);
                        } else {
                            break;
                        }
                    }
                    
                    num = 0;
                    for (int q = j; q < min(j + 3, m); ++q) {
                        if (isdigit(s2[q])) {
                            num = num * 10 + s2[q] - '0';
                            dp[i][q + 1].emplace(delta - num);
                        } else {
                            break;
                        }
                    }
                    
                    if (i < n && delta < 0 && !isdigit(s1[i])) 
                        dp[i + 1][j].emplace(delta + 1);
                            
                    if (j < m && delta > 0 && !isdigit(s2[j])) 
                        dp[i][j + 1].emplace(delta - 1);
                            
                    if (i < n && j < m && delta == 0 && s1[i] == s2[j])
                        dp[i + 1][j + 1].emplace(0);
                }
            }
        }
        
        return dp[n][m].count(0);
    }
};


// 作者：吴自华
// 链接：https://leetcode-cn.com/circle/discuss/ANhvKQ/view/TlaIUS/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。