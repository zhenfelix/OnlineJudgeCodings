class Solution {
public:
    int maximumANDSum(vector<int>& nums, int s) {
        int n = nums.size();
        vector<int> t(s + 1);
        t[0] = 1;
        for (int i = 1; i <= s; ++i)
            t[i] = t[i - 1] * 3;
        
        vector<int> dp(t[s], -1);
        dp[0] = 0;
        
        for (int num : nums) {
            for (int i = t[s] - 1; i >= 0; --i) {
                if (dp[i] == -1)
                    continue;
                
                int x = i;
                for (int j = 0; j < s; ++j) {
                    if (x % 3 < 2)
                        dp[i + t[j]] = max(dp[i + t[j]], dp[i] + (num & (j + 1)));
                    x /= 3;
                }
            }
        }

        return *max_element(dp.begin(), dp.end());
    }
};


// 作者：吴自华
// 链接：https://leetcode-cn.com/circle/discuss/oA57vT/view/OnnrrJ/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution {
public:
    int maximumANDSum(vector<int>& nums, int numSlots) {
        int n = nums.size();
        int ans = 0;
        
        vector<int> dp(1 << n, -1);
        dp[0] = 0;
        for (int s = 1; s <= numSlots; ++s) {
            for (int i = (1 << n) - 1; i >= 0; --i) {
                if (dp[i] == -1 || (__builtin_popcount(i) + (numSlots - s + 1) * 2 < n))
                    continue;
                for (int j = 0; j < n; ++j) {
                    if (i & (1 << j))
                        continue;
                    int msk = i ^ (1 << j);
                    dp[msk] = max(dp[msk], dp[i] + (nums[j] & s));
                    for (int k = j + 1; k < n; ++k) {
                        if (i & (1 << k))
                            continue;
                        dp[msk ^ (1 << k)] = max(dp[msk ^ (1 << k)], dp[i] + (nums[j] & s) + (nums[k] & s));
                    }
                }
            }
        }
        
        return dp.back();
    }
};


// 作者：吴自华
// 链接：https://leetcode-cn.com/circle/discuss/oA57vT/view/OnnrrJ/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。