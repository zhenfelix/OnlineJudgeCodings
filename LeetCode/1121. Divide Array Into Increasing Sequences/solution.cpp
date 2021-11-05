// const int maxn = 1e5+5;
// int cnt[maxn];

// class Solution {
// public:
//     bool canDivideIntoSubsequences(vector<int>& nums, int k) {
//         memset(cnt, 0, maxn*sizeof(int));
//         for (auto x : nums)
//             cnt[x]++;
//         int p = 0;
//         for (int i = 1; i < maxn; i++)
//             p = max(p, cnt[i]);
//         return p*k <= nums.size();
//     }
// };

class Solution {
public:
    bool canDivideIntoSubsequences(vector<int>& nums, int k) {
        int res = 0, cnt = 0, lk = nums[0];
        for (int k : nums) {
            if (k == lk) ++cnt;
            else res = max(res, cnt), cnt = 1, lk = k;
        }
        res = max(res, cnt);
        return res * k <= nums.size();
    }
};