class Solution {
public:
    long long countSubstrings(string s) {
        int n = s.size();

        auto gao = [&](int d) {
            long long ret = 0;
            // i 推到 i + 1 的式子常用常数优化：压缩第一维的空间
            int cnt[2][d];
            memset(cnt, 0, sizeof(cnt));
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < d; j++) cnt[i & 1][j] = 0;
                // 套用递推式
                for (int j = 0; j < d; j++) {
                    int v = (j * 10 + s[i] - '0') % d;
                    cnt[i & 1][v] += cnt[i & 1 ^ 1][j];
                }
                cnt[i & 1][(s[i] - '0') % d]++;
                // 把所有 s[i] == d 的位置的 f(i, 0) 加起来就是答案
                if (s[i] - '0' == d) ret += cnt[i & 1][0];
            }
            return ret;
        };

        long long ans = 0;
        // 枚举最后一位数码是什么
        for (int i = 1; i < 10; i++) ans += gao(i);
        return ans;
    }
};

作者：TsReaper
链接：https://leetcode.cn/problems/count-substrings-divisible-by-last-digit/solutions/3068717/mei-ju-di-tui-by-tsreaper-62rp/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。