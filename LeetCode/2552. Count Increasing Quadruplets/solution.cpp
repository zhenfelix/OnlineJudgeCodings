// c++ 有栈大小限制，只好开全局数组
int f[4010][4010], g[4010][4010];

class Solution {
public:
    long long countQuadruplets(vector<int>& nums) {
        int n = nums.size();
        // 计算二维前缀和
        for (int i = 0; i <= n + 1; i++) for (int j = 0; j <= n + 1; j++) f[i][j] = g[i][j] = 0;
        for (int i = 1; i <= n; i++) f[i][nums[i - 1]] = g[i][nums[i - 1]] = 1;
        for (int i = 1; i <= n; i++) for (int j = 1; j <= n; j++) f[i][j] += f[i][j - 1];
        for (int i = 1; i <= n; i++) for (int j = 1; j <= n; j++) f[i][j] += f[i - 1][j];
        for (int i = n; i > 0; i--) for (int j = n; j > 0; j--) g[i][j] += g[i][j + 1];
        for (int i = n; i > 0; i--) for (int j = n; j > 0; j--) g[i][j] += g[i + 1][j];

        // 枚举 j 和 k，计算答案
        long long ans = 0;
        for (int j = 1; j <= n; j++) for (int k = j + 1; k <= n; k++) if (nums[j - 1] > nums[k - 1])
            ans += 1LL * f[j - 1][nums[k - 1] - 1] * g[k + 1][nums[j - 1] + 1];
        return ans;
    }
};


// 作者：TsReaper
// 链接：https://leetcode.cn/circle/discuss/LWLEFc/view/wH1HCi/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。