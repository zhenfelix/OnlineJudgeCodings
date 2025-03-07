class Solution {
public:
    long long countNonDecreasingSubarrays(vector<int>& nums, int K) {
        int n = nums.size();
        // 前缀和
        long long f[n];
        f[0] = nums[0];
        for (int i = 1; i < n; i++) f[i] = f[i - 1] + nums[i];

        // R[i]：下一个大于等于 nums[i] 的元素在哪
        int R[n];
        for (int i = 0; i < n; i++) R[i] = n;
        // vec[i]：nums[i] 是哪些数的“左边最近的更大数”
        vector<int> vec[n];
        // 单调栈
        stack<int> stk;
        for (int i = 0; i < n; i++) {
            while (!stk.empty() && nums[stk.top()] <= nums[i]) R[stk.top()] = i, stk.pop();
            if (!stk.empty()) vec[stk.top()].push_back(i);
            stk.push(i);
        }

        // 计算 nums[i] 对右边数的覆盖情况，最多计算到 nums[lim]
        auto calc = [&](int i, int lim) {
            lim = min(lim, R[i] - 1);
            return 1LL * nums[i] * (lim - i) - (f[lim] - f[i]);
        };

        long long ans = 0, now = 0;
        // 双端队列维护单调队列
        deque<int> dq;
        // 双指针：i 是子数组的末尾，j 是子数组的开头最左边能到哪里
        for (int i = 0, j = 0; i < n; i++) {
            // 将 nums[i] 加入单调队列
            while (!dq.empty() && nums[dq.back()] <= nums[i]) dq.pop_back();
            dq.push_back(i); now += nums[dq.front()] - nums[i];
            while (j < i && now > K) {
                // 扣掉被去掉的元素的贡献
                now -= calc(j, i);
                for (int x : vec[j]) {
                    // 加上露出来的元素的贡献
                    if (x > i) break;
                    now += calc(x, i);
                }
                // 如有必要，从单调队列中去掉 nums[j]
                if (dq.front() == j) dq.pop_front();
                j++;
            }
            ans += i - j + 1;
        }
        return ans;
    }
};

// 作者：TsReaper
// 链接：https://leetcode.cn/problems/count-non-decreasing-subarrays-after-k-operations/solutions/3045049/shuang-zhi-zhen-dan-diao-zhan-dan-diao-d-hmt6/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。