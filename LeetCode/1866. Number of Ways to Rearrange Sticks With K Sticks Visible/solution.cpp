class Solution {
public:
    bool vis[1005][1005];
    int f[1005][1005];
    const int mod = (int )1e9 + 7;
    int dp(int n, int k) {
        if (n == 0 && k == 0) return 1;
        if (k == 0) return 0;
        if (n == 0) return 0;
        if (vis[n][k]) return f[n][k];
        vis[n][k] = true;
        return f[n][k] = (1LL * (n - 1) * dp(n - 1, k) + dp(n - 1, k - 1)) % mod;
    }
    int rearrangeSticks(int n, int k) {
        return dp(n, k);
    }
};


class Solution {
private:
    static constexpr int mod = 1000000007;
    
public:
    int rearrangeSticks(int n, int k) {
        vector<int> f(k + 1);
        f[0] = 1;
        for (int i = 1; i <= n; ++i) {
            vector<int> g(k + 1);
            for (int j = 1; j <= k; ++j) {
                g[j] = ((long long)f[j] * (i - 1) % mod + f[j - 1]) % mod;
            }
            // cout << g[0] << endl;
            f = move(g);
        }
        return f[k];
    }
};


// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/solution/qia-you-k-gen-mu-gun-ke-yi-kan-dao-de-pa-0c3g/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。