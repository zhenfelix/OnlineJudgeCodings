class Solution {
public:
    long long maxStrength(vector<int>& nums) {
        int n = nums.size();
        // 把正数、负数、零分开记录
        vector<int> neg, pos;
        int zero = 0;
        for (int x : nums) {
            if (x > 0) pos.push_back(x);
            else if (x < 0) neg.push_back(x);
            else zero++;
        }
        sort(neg.begin(), neg.end());

        // 先按“选出所有正数，以及偶数个绝对值最大的负数”的策略来选择
        // cnt 表示这个策略选出了几个数
        long long ans = 1;
        int cnt = 0;
        for (int x : pos) ans *= x, cnt++;
        for (int i = 0; i + 1 < neg.size(); i += 2) ans *= neg[i] * neg[i + 1], cnt += 2;
        // 这个策略至少选了一个数，可以返回答案
        if (cnt > 0) return ans;
        else {
            // 这个策略没选出数，那答案肯定不是正数了，讨论特殊情况
            // 情况 1：答案最大只能是 0 了，所以有 0 选 0
            if (zero > 0) return 0;
            // 情况 2：连 0 都没有，那只能选最大的负数
            else return nums[0];
        }
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/fQ58lb/view/6vKWNF/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。