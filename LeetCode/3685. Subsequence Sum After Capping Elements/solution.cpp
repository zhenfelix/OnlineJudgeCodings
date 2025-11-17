class Solution {
public:
    vector<bool> subsequenceSumAfterCapping(vector<int>& nums, int K) {
        int n = nums.size();
        sort(nums.begin(), nums.end());

        bool f[K + 1];
        memset(f, 0, sizeof(f));
        f[0] = true;

        // 上限为 x，且有 y 个元素超出上限的数组，能否组合出 k
        auto check = [&](int x, int y) {
            // 枚举选几个超出上限的元素
            for (int i = 0; i <= y; i++) {
                int det = K - x * i;
                if (det < 0) break;
                // 看前缀能否组合出差值
                if (f[det]) return true;
            }
            return false;
        };

        vector<bool> ans;
        // 所有元素都超出上限的情况
        for (int i = 1; i < nums[0]; i++) ans.push_back(check(i, n));
        // 01 背包求前 i 个数能组合出几种元素和
        for (int i = 0; i < n; i++) {
            for (int j = K; j >= nums[i]; j--) if (f[j - nums[i]]) f[j] = true;
            // 前 i 个元素不超出上限的情况
            for (int j = nums[i]; j < (i + 1 < n ? nums[i + 1] : n + 1); j++) ans.push_back(check(j, n - 1 - i));
        }
        return ans;
    }
};

作者：TsReaper
链接：https://leetcode.cn/problems/subsequence-sum-after-capping-elements/solutions/3781341/bei-bao-dp-mei-ju-by-tsreaper-nj4t/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。