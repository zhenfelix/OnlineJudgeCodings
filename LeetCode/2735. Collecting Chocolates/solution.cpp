class Solution {
public:
    long long minCost(vector<int>& nums, int x) {
        int n = nums.size();

        // 预处理 f[i][j] 表示进行 j 次类型修改操作后，类型为 i 的巧克力的最小代价
        int f[n][n];
        for (int i = 0; i < n; i++) f[i][0] = nums[i];
        for (int i = 0; i < n; i++) for (int j = 1; j < n; j++) f[i][j] = min(f[i][j - 1], nums[(i - j + n) % n]);

        long long ans = 1e18;
        // 枚举类型修改操作的次数
        for (int k = 0; k < n; k++) {
            // 计算所有巧克力最小代价之和
            long long tmp = 0;
            for (int i = 0; i < n; i++) tmp += f[i][k];
            // 代价还要加上类型修改操作的代价
            ans = min(ans, tmp + 1LL * k * x);
        }
        return ans;
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/bvOqiS/view/FomS8E/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。