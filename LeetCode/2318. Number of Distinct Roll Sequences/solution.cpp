const int MOD = 1e9 + 7, MX = 1e4;
int f[MX + 1][6][6];
int init = []() {
    for (int i = 0; i < 6; ++i)
        for (int j = 0; j < 6; ++j)
            f[2][i][j] = j != i && gcd(j + 1, i + 1) == 1;
    for (int i = 2; i < MX; ++i)
        for (int j = 0; j < 6; ++j)
            for (int last = 0; last < 6; ++last)
                if (last != j && gcd(last + 1, j + 1) == 1)
                    for (int last2 = 0; last2 < 6; ++last2)
                        if (last2 != j)
                            f[i + 1][j][last] = (f[i + 1][j][last] + f[i][last][last2]) % MOD;
    return 0;
}();

class Solution {
public:
    int distinctSequences(int n) {
        if (n == 1) return 6;
        int ans = 0;
        for (int i = 0; i < 6; ++i)
            for (int j = 0; j < 6; ++j)
                ans = (ans + f[n][i][j]) % MOD;
        return ans;
    }
};


作者：endlesscheng
链接：https://leetcode.cn/problems/number-of-distinct-roll-sequences/solution/by-endlesscheng-tgkn/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。