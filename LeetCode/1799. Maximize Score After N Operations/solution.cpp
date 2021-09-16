// class Solution
// {
// public:
//     int maxScore(vector<int> &nums)
//     {
//         int n = nums.size();
//         vector<int> dp(1 << n, 0);
//         for (int i = 1; i < (1 << n); i++)
//         {
//             int m = __builtin_popcount(i);
//             if (m & 1)
//                 continue;
//             for (int j = 0; j < n; j++)
//             {
//                 if ((i >> j) & 1){
//                     for (int k = j + 1; k < n; k++)
//                     {
//                         if ((i >> k) & 1)
//                         {
//                             // cout << i << " " << i - (1 << j) - (1 << k) << " " << j << " " << k << endl;
//                             dp[i] = max(dp[i], dp[i - (1 << j) - (1 << k)] + __gcd(nums[j], nums[k]) * m / 2);
//                         }
//                     }
//                 }
                
//             }
//         }
//         return dp.back();
//     }
// };


class Solution
{
public:
    int maxScore(vector<int> &nums)
    {
        int n = nums.size();
        vector<int> dp(1 << n, 0);
        for (int i = 1; i < (1 << n); i++)
        {
            int m = __builtin_popcount(i);
            if (m & 1)
                continue;
            for (int j = 0; j < n; j++)
            {
                if (((i >> j) & 1) == 0)
                    continue;
                for (int k = j + 1; k < n; k++)
                {
                    if (((i >> k) & 1) == 0)
                        continue;
                    // cout << i << " " << i - (1 << j) - (1 << k) << " " << j << " " << k << endl;
                    dp[i] = max(dp[i], dp[i - (1 << j) - (1 << k)] + __gcd(nums[j], nums[k]) * m / 2);
                }
            }
        }
        return dp.back();
    }
};