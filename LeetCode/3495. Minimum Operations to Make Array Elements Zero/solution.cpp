class Solution {
public:
    long long minOperations(vector<vector<int>>& queries) {
        // 计算 [1, x] 的操作次数之和
        auto calc = [&](long long x) {
            long long ret = 0;
            long long p = 1;
            // [p, 4p) 范围内的元素，操作次数均为 i
            for (int i = 1; p <= x; i++, p *= 4) {
                long long cnt = min(p * 4 - 1, x) - p + 1;
                ret += cnt * i;
            }
            return ret;
        };

        long long ans = 0;
        for (auto &qry : queries) {
            int l = qry[0], r = qry[1];
            ans += max(
                // 用前缀和算出 [l, r] 操作次数之和 s，这里求的是 ceil(s / 2)
                (calc(r) - calc(l - 1) + 1) / 2,
                // 用前缀和算出 r 的操作次数，因为元素越大，操作次数最大
                calc(r) - calc(r - 1)
            );
        }
        return ans;
    }
};

作者：TsReaper
链接：https://leetcode.cn/problems/minimum-operations-to-make-array-elements-zero/solutions/3624234/qian-zhui-he-by-tsreaper-atc0/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。