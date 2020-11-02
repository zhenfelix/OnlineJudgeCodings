class Solution {
public:
    int countSubstrings(string s, string t) {
        int m = s.size();
        int n = t.size();
        int ans = 0;
        for (int delta = -m + 1; delta < n; ++delta) {
            // 我们枚举每一个边界条件 (i,0) 以及 (0,j)
            int i = 0, j = 0;
            if (delta > 0) {
                j = delta;
            }
            else {
                i = -delta;
            }
            // f(i,j) 和 g(i,j) 的初始值均为 0
            int fij = 0, gij = 0;
            for (; i < m && j < n; ++i, ++j) {
                if (s[i] == t[j]) {
                    // f(i,j) 不变，g(i,j) 加 1
                    ++gij;
                }
                else {
                    // f(i,j) 变为 g(i,j) 加 1，g(i,j) 置零
                    fij = gij + 1;
                    gij = 0;
                }
                ans += fij;
            }
        }
        return ans;
    }
};


// 作者：zerotrac2
// 链接：https://leetcode-cn.com/problems/count-substrings-that-differ-by-one-character/solution/tong-ji-zhi-chai-yi-ge-zi-fu-de-zi-chuan-shu-mu-by/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

// class Solution {
// public:
//     int countSubstrings(string &s, string &t) {
//     int res = 0;
//     int dpl[101][101] = {}, dpr[101][101] = {};
//     for (int i = 1; i <= s.size(); ++i)
//         for (int j = 1; j <= t.size(); ++j)
//             if (s[i - 1] == t[j - 1])
//                 dpl[i][j] = 1 + dpl[i - 1][j - 1];
//     for (int i = s.size(); i > 0; --i)
//         for (int j = t.size(); j > 0; --j)
//             if (s[i - 1] == t[j - 1])
//                 dpr[i - 1][j - 1] = 1 + dpr[i][j];
//     for (int i = 0; i < s.size(); ++i)
//         for (int j = 0; j < t.size(); ++j)
//             if (s[i] != t[j])
//                 res += (dpl[i][j] + 1) * (dpr[i + 1][j + 1] + 1);
//     return res;
// }
// };