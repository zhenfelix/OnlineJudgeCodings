class Solution {
    const int MOD = 1000000007;

public:
    long long sumScores(string s) {
        int n = s.size();
        vector<long long> f(n + 1), P(n + 1);
        for (int i = 1; i <= n; i++) f[i] = (f[i - 1] * 171 + s[i - 1]) % MOD;
        P[0] = 1;
        for (int i = 1; i <= n; i++) P[i] = P[i - 1] * 171 % MOD;

        long long ans = 0;
        for (int i = n; i; i--) {
            int head = 0, tail = n - i + 1;
            while (head < tail) {
                int mid = (head + tail + 1) >> 1;
                long long h = (f[i + mid - 1] - f[i - 1] * P[mid] % MOD + MOD) % MOD;
                if (h == f[mid]) head = mid;
                else tail = mid - 1;
            }
            ans += head;
        }
        return ans;
    }
};


作者：tsreaper
链接：https://leetcode.cn/problems/sum-of-scores-of-built-strings/solution/by-tsreaper-weu5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。