class Solution {
public:
    long long maxSumTrionic(vector<int>& nums) {
        int n = nums.size();

        const long long INF = 1e18;
        long long f[n][3];
        for (int i = 0; i < n; i++) for (int j = 0; j < 3; j++) f[i][j] = -INF;

        long long ans = -INF;
        for (int i = 0; i < n; i++) {
            // 从 nums[i] 开启一个新的子数组
            f[i][0] = nums[i];
            if (i > 0 && nums[i] > nums[i - 1]) {
                long long t = f[i - 1][0] + nums[i];
                // nums[i] 接续之前的第一段
                f[i][0] = max(f[i][0], t);
                // 从 nums[i] 开启第二段
                f[i][1] = max(f[i][1], t);
            }
            if (i > 0 && nums[i] < nums[i - 1]) {
                long long t = f[i - 1][1] + nums[i];
                // nums[i] 接续之前的第二段
                f[i][1] = max(f[i][1], t);
                // 从 nums[i] 开启第三段
                f[i][2] = max(f[i][2], t);
            }
            if (i > 0 && nums[i] > nums[i - 1]) {
                long long t = f[i - 1][2] + nums[i];
                // nums[i] 接续之前的第三段
                f[i][2] = max(f[i][2], t);
                // 子数组结束
                ans = max(ans, t);
            }
        }
        return ans;
    }
};

作者：TsReaper
链接：https://leetcode.cn/problems/trionic-array-ii/solutions/3741022/dp-by-tsreaper-kq8g/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。