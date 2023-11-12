class Solution {
public:
    int minimumChanges(string s, int K) {
        int n = s.size();

        const int INF = 1e9;
        int g[n + 1][n + 1];
        for (int i = 0; i <= n; i++) for (int j = 0; j <= n; j++) g[i][j] = INF;
        // 枚举每个子串，计算变成半回文串要修改几次
        for (int i = 1; i <= n; i++) for (int j = i; j <= n; j++) {
            int len = j - i + 1;
            // 枚举因数 d
            for (int d = 1; d < len; d++) if (len % d == 0) {
                int cnt = 0;
                // 枚举每个字符，并检查它对应的字符
                for (int k = 0; k < len; k++) {
                    int kk = (len / d - 1 - k / d) * d + k % d;
                    if (k >= kk) break;
                    if (s[i - 1 + k] != s[i - 1 + kk]) cnt++;
                }
                g[i][j] = min(g[i][j], cnt);
            }
        }

        // 套 dp 方程
        int f[n + 1][K + 1];
        for (int i = 0; i <= n; i++) for (int j = 0; j <= K; j++) f[i][j] = INF;
        f[0][0] = 0;
        for (int i = 1; i <= n; i++) for (int j = 1; j <= K; j++) for (int ii = i - 1; ii >= 0; ii--)
            f[i][j] = min(f[i][j], f[ii][j - 1] + g[ii + 1][i]);
        return f[n][K];
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/haZ1d7/view/dUbwkm/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution {
public:
    int minimumChanges(string s, int k) {
        int n = s.length();
        vector<vector<int>> dp(n,vector<int>(n,n));
        vector<vector<int>> cnt(n,vector<int>(n,0));
        for(int d = 1; d <= n; d++){
            for (int sz = d*2; sz <= n; sz+=d){
                for (int i = 0; i+sz <= n; i++) {
                    for (int j = 0; j < sz/2; j++) {
                        if (s[i+j] != s[i+(sz/d-j/d-1)*d+j%d]) cnt[i][i+sz-1]++;
                    }
                }
            }
            for(int i=0;i<n;i++)for(int j=i+d*2-1;j<n;j+=d){
                dp[i][j] = min(dp[i][j],cnt[i][j]);
                cnt[i][j] = 0;
            }
        }
        vector<int> f = dp[0];
        for (int kk = 1; kk < k; kk++){
            for (int j = n-1; j >= 0; j--){
                f[j]=n;
                for (int i = 0;i < j;i++) f[j] = min(f[j],f[i]+dp[i+1][j]);
            }
        }
        return f[n-1];

    }
};