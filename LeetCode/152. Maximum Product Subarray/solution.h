class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n=nums.size(),ans,dp,dpMin;
        dp=nums[0];ans=dp;dpMin=dp;
        for(int i=1;i<n;i++){
            int tmp=max(nums[i]*dpMin, max(nums[i]*dp,nums[i]));
            dpMin=min(nums[i]*dpMin, min(nums[i]*dp,nums[i]));
            dp=tmp;
            ans=max(ans,dp);
        }
        return ans;
    }
};