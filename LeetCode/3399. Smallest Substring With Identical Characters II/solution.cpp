class Solution {
public:
    int minLength(string s, int numOps) {
        int n = s.size();

        // 枚举两种最终字符串，特判答案是 1 的情况
        auto gao = [&](int x) {
            int cnt = 0;
            for (int i = 0; i < n; i++) if (s[i] % 2 != (i + x) % 2) cnt++;
            return cnt <= numOps;
        };
        if (gao(0) || gao(1)) return 1;

        // 能否用最多 numOps 次操作，不让连续 lim + 1 个字符相同
        auto check = [&](int lim) {
            int cnt = 0;
            for (int i = 0, j = 0; i < n; i++) if (i == n - 1 || s[i] != s[i + 1]) {
                int len = i - j + 1;
                cnt += len / (lim + 1);
                j = i + 1;
            }
            return cnt <= numOps;
        };

        // 二分答案
        int head = 2, tail = n;
        while (head < tail) {
            int mid = (head + tail) >> 1;
            if (check(mid)) tail = mid;
            else head = mid + 1;
        }
        return head;
    }
};



作者：TsReaper
链接：https://leetcode.cn/circle/discuss/o32MNN/view/SSyeKC/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。