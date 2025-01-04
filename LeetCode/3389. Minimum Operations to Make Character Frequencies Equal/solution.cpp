class Solution {
public:
    int makeStringGood(string s) {
        int n = s.size();
        // 统计每种字母出现次数
        int cnt[27] = {0};
        for (char c : s) cnt[c - 'a' + 1]++;

        // 求每种字母出现 Y 次的最少操作次数
        auto gao = [&](int Y) {
            const int INF = 1e9;
            int f[27][2];
            for (int i = 0; i <= 26; i++) f[i][0] = f[i][1] = INF;
            f[0][0] = 0;
            for (int i = 1; i <= 26; i++) {
                // 转移一
                f[i][0] = min(f[i - 1][0], f[i - 1][1]) + cnt[i];
                // 转移二
                if (cnt[i] >= Y) f[i][1] = min(f[i - 1][0], f[i - 1][1]) + cnt[i] - Y;
                else {
                    int det = Y - cnt[i];
                    f[i][1] = min(
                        // 转移三
                        f[i - 1][0] + det - min(det, cnt[i - 1]),
                        // 转移四
                        f[i - 1][1] + det - min(det, max(0, cnt[i - 1] - Y))
                    );
                }
            }
            return min(f[26][0], f[26][1]);
        };

        int ans = n;
        // 枚举字母频率
        for (int j = 1; j <= n; j++) ans = min(ans, gao(j));
        return ans;
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/NPtUvN/view/HulXaw/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。