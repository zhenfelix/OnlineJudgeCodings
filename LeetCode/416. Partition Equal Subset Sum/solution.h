class Solution {
public:
    bool helper(int idx, int target, vector<int> &nums){
        if(target==nums[idx])return true;
        if(target<nums[idx])return false;//important ending condition??
        return helper(idx+1,target-nums[idx],nums)||helper(idx+1,target,nums);
    }
    bool canPartition(vector<int>& nums) {
        int sums=0;
        for(auto x: nums)sums+=x;
        if(sums%2!=0)return false;
        sort(nums.begin(),nums.end(),greater<int>());
        return helper(0,sums/2,nums);
    }
};
 // Time Limit Exceeded


// class Solution {
// public:
//     bool canPartition(vector<int>& nums) {
//         int sum = 0;
//         for(int i =0;i<nums.size();i++){
//             sum+= nums[i];
//         }
//         if(sum%2) return false;
//         sum /= 2;
//         sort(nums.begin(),nums.end(),greater<int>());
//         return helper(nums, sum, 0);
//     }
//     bool helper(vector<int>& nums, int sum, int index){
//         if(sum == nums[index]) return true;
//         if(sum < nums[index]) return false;
//         return helper(nums,sum-nums[index],index+1) || helper(nums,sum,index+1);
//     }
// };



// class Solution {
// public:

//     bool canPartition(vector<int>& nums) {
//         int sums=0,n=nums.size();
//         for(auto x: nums)sums+=x;
//         if(sums%2!=0)return false;
//         sums/=2;
//         vector<vector<bool>> dp(n+1,vector<bool>(sums+1,false));
        
//         dp[0][0]=true;
//         for(int i=1;i<=n;i++)dp[i][0]=true;
//         for(int j=1;j<=sums;j++)dp[0][j]=false;
//         for(int i=1;i<=n;i++){
//             for(int j=1;j<=sums;j++){
//                 dp[i][j]=dp[i-1][j];
//                 if(nums[i-1]<=j)dp[i][j]=dp[i-1][j-nums[i-1]]||dp[i][j];
//             }
//         }
//         return dp[n][sums];
//     }
// };