class Solution {
public:
    int beautifulSubsets(vector<int>& nums, int k) {
        int n = nums.size();
        int mx = 0;
        for (int x : nums) mx = max(mx, x);

        // vis[i] 表示目前子集中有几个 i
        int vis[mx + 1];
        memset(vis, 0, sizeof(vis));

        int ans = 0;
        function<void(int)> dfs = [&](int pos) {
            // dfs 结束，是合法子集
            if (pos == n) { ans++; return; }

            // === 分支 1：尝试把第 pos 个数加入子集 ===
            vis[nums[pos]]++;
            // 检查是否存在 nums[pos] + k 和 nums[pos] - k
            bool flag = true;
            if (nums[pos] + k <= mx && vis[nums[pos] + k] > 0) flag = false;
            if (nums[pos] - k >= 0 && vis[nums[pos] - k] > 0) flag = false;
            // 若检查通过则可以把第 pos 个数加入子集
            if (flag) dfs(pos + 1);
            // 撤销第 pos 个数的影响
            vis[nums[pos]]--;

            // === 分支 2：第 pos 个数不加入子集 ===
            dfs(pos + 1);
        };
        dfs(0);
        // 题目要求非空子集，答案减 1
        return ans - 1;
    }
};


// 作者：TsReaper
// 链接：https://leetcode.cn/circle/discuss/4MTE6Z/view/1qfLru/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。