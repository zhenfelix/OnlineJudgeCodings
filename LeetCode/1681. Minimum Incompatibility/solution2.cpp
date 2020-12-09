class Solution {
public:
    int minimumIncompatibility(vector<int>& nums, int k) {
        int n = nums.size(), per = n/k;
        if(k == 1) {
            set<int> s(nums.begin(), nums.end());
            if(s.size() < nums.size()) {
                return -1;
            }
            return (*s.rbegin()) - (*s.begin());
        }
        if(k == n) {
            return 0;
        }
        sort(nums.begin(), nums.end());
        int M = (1 << n), dp[M][n], cnts[M];
        for(int i = 0; i < M; ++i) {
            int cur = 0;
            for(int j = 0; j < n; ++j) {
                if(i & (1 << j)) {
                    cur += 1;
                }
            }
            cnts[i] = cur;
        }
        memset(dp, 0x3f, sizeof(dp));
        memset(dp[0], 0, sizeof(dp[0]));
        for(int mask = 1; mask < M; ++mask) {
            if((cnts[mask] % per) == 0) {
                for(int p = 0; p < n; ++p) {
                    if(mask & (1 << p)) {
                        dp[mask][0] = min(dp[mask][0], dp[mask ^ (1 << p)][p]);
                    }
                }
                for(int pre = 1; pre < n; ++pre) {
                    dp[mask][pre] = dp[mask][0];
                }
            } else {
                for(int pre = 0; pre < n; ++pre) {
                    for(int p = pre + 1; p < n; ++p) {
                        if((mask & (1 << p)) && nums[p] > nums[pre]) {
                            dp[mask][pre] = min(dp[mask][pre], dp[mask ^ (1 << p)][p] + nums[p] - nums[pre]);
                        }
                    }
                }
            }
        }
        if(dp[M-1][0] >= 10000) {
            return -1;
        }
        return dp[M-1][0];
    }
};


作者：newhar
链接：https://leetcode-cn.com/problems/minimum-incompatibility/solution/lao-tao-lu-zhuang-tai-ya-suo-dp-by-newha-j58b/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。