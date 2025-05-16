class Solution {
public:
    long long maxSubarrays(int n, vector<vector<int>>& pairs) {
        int m = pairs.size();

        // col[i]：元素 i 有哪些记号
        vector<int> col[n + 1];
        for (int i = 0; i < m; i++) {
            col[pairs[i][0]].push_back(i + 1);
            col[pairs[i][1]].push_back(i + 1);
        }

        // f[i]：以下标 i 为结尾的，不含重复记号的子数组最长是多少
        // g[i]：以下标 i 为结尾的，含一种重复记号的子数组最长是多少
        // h[i]：重复记号具体是哪个
        int f[n + 1], g[n + 1], h[n + 1];

        // 双指针求不含重复记号的子数组
        int cnt[m + 1];
        memset(cnt, 0, sizeof(cnt));
        int bad = 0;
        for (int i = 1, j = 1; i <= n; i++) {
            for (int x : col[i]) {
                int t = ++cnt[x];
                if (t == 2) bad++;
            }
            while (j <= i && bad > 0) {
                for (int x : col[j]) {
                    int t = --cnt[x];
                    if (t == 1) bad--;
                }
                j++;
            }
            f[i] = i - j + 1;
        }

        // 双指针求最多含一种重复记号的子数组
        memset(cnt, 0, sizeof(cnt));
        bad = 0;
        long long sm = 0;
        for (int i = 1, j = 1; i <= n; i++) {
            for (int x : col[i]) {
                int t = ++cnt[x];
                if (t == 2) bad++, sm += x;
            }
            while (j <= i && bad > 1) {
                for (int x : col[j]) {
                    int t = --cnt[x];
                    if (t == 1) bad--, sm -= x;
                }
                j++;
            }
            g[i] = i - j + 1;
            // 如果子数组里没有重复记号，h[i] 就是 0
            h[i] = sm;
        }

        // val[i]：重复记号 i 对答案的贡献
        long long val[m + 1];
        memset(val, 0, sizeof(val));
        long long base = 0;
        for (int i = 1; i <= n; i++) {
            base += f[i];
            val[h[i]] += g[i] - f[i];
        }
        long long best = 0;
        // 选择保留哪种重复记号
        for (int i = 1; i <= m; i++) best = max(best, val[i]);
        return base + best;
    }
};