class Solution {
public:
    long long minimumCost(vector<int>& nums, vector<int>& cost, int K) {
        int n = nums.size();

        // 求 nums 和 cost 的前缀和
        long long sn[n + 1], sc[n + 1];
        sn[0] = sc[0] = 0;
        for (int i = 1; i <= n; i++) {
            sn[i] = sn[i - 1] + nums[i - 1];
            sc[i] = sc[i - 1] + cost[i - 1];
        }

        const long long INF = 1e18;
        long long f[n + 1];
        for (int i = 0; i <= n; i++) f[i] = INF;
        f[0] = 0;
        // 套 DP 方程
        for (int i = 1; i <= n; i++) for (int j = 0; j < i; j++) {
            long long t = sn[i] * (sc[i] - sc[j]) + K * (sc[n] - sc[j]);
            f[i] = min(f[i], f[j] + t);
        }

        return f[n];
    }
};

作者：TsReaper
链接：https://leetcode.cn/problems/minimum-cost-to-divide-array-into-subarrays/solutions/3633239/qian-zhui-he-dp-by-tsreaper-7g2c/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。