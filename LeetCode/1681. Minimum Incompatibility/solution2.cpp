int dp[(1 << 16)*16];
class Solution {
public:
    int n, per, maxv = 1e9;
    vector<int> nums;
    int lowbit(int x) { return x & (-x); } // lowbit 函数：求出当前数字最低位的 1。
    int f(int mask, int pre) {
        if(mask == 0) {
            return 0;
        }
        if(dp[mask * n + pre] != -1) {
            return dp[mask * n + pre];
        }
        int cnt = __builtin_popcount(mask), rem = cnt % per, res = maxv;
        if(rem == 0) { // 当前要为新子集分配数字
            res = f(mask ^ lowbit(mask),  __builtin_ctz(mask)); // 剪枝：我们不妨从第一个可用的数字开始为新子集分配数字。
            for(int pre = 0; pre < n; ++pre) {
                dp[mask*n + pre] = res; // 此时 pre 的数值不重要
            }
        } else { // 当前子集已经有了数字 nums[pre]，继续分配
            if(__builtin_popcount(mask >> (pre + 1)) >= rem) { // 剪枝：剩余可用数字的个数必须足够填充当前子集
                for(int p = pre + 1; p < n; ++p) {
                    if((mask & (1 << p)) && nums[p] > nums[pre]) {
                        res = min(res, f(mask ^ (1 << p), p) + nums[p] - nums[pre]);
                    }
                }
            }
            dp[mask*n + pre] = res;
        }
        return res;
    }
    int minimumIncompatibility(vector<int>& nums, int k) {
        n = nums.size(), per = n/k;
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
        this->nums = nums;
        memset(dp, -1, (1 << n)*n*sizeof(int));
        
        int res = f((1 << n) - 1, 0);
        if(res >= 10000) {
            return -1;
        }
        return res;
    }
};


作者：newhar
链接：https://leetcode-cn.com/problems/minimum-incompatibility/solution/lao-tao-lu-zhuang-tai-ya-suo-dp-by-newha-j58b/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。




// class Solution {
// public:
//     int minimumIncompatibility(vector<int>& nums, int k) {
//         int n = nums.size(), per = n/k;
//         if(k == 1) {
//             set<int> s(nums.begin(), nums.end());
//             if(s.size() < nums.size()) {
//                 return -1;
//             }
//             return (*s.rbegin()) - (*s.begin());
//         }
//         if(k == n) {
//             return 0;
//         }
//         sort(nums.begin(), nums.end());
//         int M = (1 << n), dp[M][n], cnts[M];
//         for(int i = 0; i < M; ++i) {
//             int cur = 0;
//             for(int j = 0; j < n; ++j) {
//                 if(i & (1 << j)) {
//                     cur += 1;
//                 }
//             }
//             cnts[i] = cur;
//         }
//         memset(dp, 0x3f, sizeof(dp));
//         memset(dp[0], 0, sizeof(dp[0]));
//         for(int mask = 1; mask < M; ++mask) {
//             if((cnts[mask] % per) == 0) {
//                 for(int p = 0; p < n; ++p) {
//                     if(mask & (1 << p)) {
//                         dp[mask][0] = min(dp[mask][0], dp[mask ^ (1 << p)][p]);
//                     }
//                 }
//                 for(int pre = 1; pre < n; ++pre) {
//                     dp[mask][pre] = dp[mask][0];
//                 }
//             } else {
//                 for(int pre = 0; pre < n; ++pre) {
//                     for(int p = pre + 1; p < n; ++p) {
//                         if((mask & (1 << p)) && nums[p] > nums[pre]) {
//                             dp[mask][pre] = min(dp[mask][pre], dp[mask ^ (1 << p)][p] + nums[p] - nums[pre]);
//                         }
//                     }
//                 }
//             }
//         }
//         if(dp[M-1][0] >= 10000) {
//             return -1;
//         }
//         return dp[M-1][0];
//     }
// };


// 作者：newhar
// 链接：https://leetcode-cn.com/problems/minimum-incompatibility/solution/lao-tao-lu-zhuang-tai-ya-suo-dp-by-newha-j58b/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。