#include <vector>
#include <map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum=0,ans=nums[0];
        for(int i=0;i<nums.size();i++){
            sum+=nums[i];
            ans=max(ans,sum);
            sum=max(0,sum);
        }
        return ans;
    }
};

// public int maxSubArray(int[] A) {
//         int n = A.length;
//         int[] dp = new int[n];//dp[i] means the maximum subarray ending with A[i];
//         dp[0] = A[0];
//         int max = dp[0];
        
//         for(int i = 1; i < n; i++){
//             dp[i] = A[i] + (dp[i - 1] > 0 ? dp[i - 1] : 0);
//             max = Math.max(max, dp[i]);
//         }
        
//         return max;
// }