// const int maxn = 2e5+10;
// int mi[maxn], mx[maxn], sums[maxn];

// class Solution {
// public:
//     int minMoves(vector<int>& nums, int limit) {
//         memset(mi,0,(limit*2+1)*sizeof(int));
//         memset(mx,0,(limit*2+1)*sizeof(int));
//         memset(sums,0,(limit*2+1)*sizeof(int));
//         int n = nums.size();
//         int m = n/2;
//         for (int i = 0; i < m; i++){
//             sums[nums[i]+nums[n-1-i]]++;
//             mi[min(nums[i],nums[n-1-i])]++;
//             mx[max(nums[i],nums[n-1-i])]++;
//         }
//         for (int i = 1; i <= limit*2; i++){
//             mi[i] += mi[i-1];
//             mx[i] += mx[i-1];
//         }
//         int res = n;
//         for (int i = 2; i <= limit*2; i++){
//             int down = i-limit-1 > 0 ? mx[i-limit-1] : 0;
//             int up = m-mi[i-1];
//             res = min(res, m-sums[i]+up+down);
//         }
//         return res;
//     }
// };


class Solution {
public:
    int minMoves(vector<int>& nums, int limit) {
        int n = nums.size();
        vector<int> delta(limit * 2 + 2);
        for (int i = 0; i < n / 2; ++i) {
            int lo = 1 + min(nums[i], nums[n - i - 1]);
            int hi = limit + max(nums[i], nums[n - i - 1]);
            int sum = nums[i] + nums[n - i - 1];
            delta[lo]--;
            delta[sum]--;
            delta[sum + 1]++;
            delta[hi + 1]++;
        }
        int now = n;
        int ans = n;
        for (int i = 2; i <= limit * 2; ++i) {
            now += delta[i];
            ans = min(ans, now);
        }
        return ans;
    }
};


// 作者：lucifer1004
// 链接：https://leetcode-cn.com/problems/minimum-moves-to-make-array-complementary/solution/chai-fen-sao-miao-by-lucifer1004/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。