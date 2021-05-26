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