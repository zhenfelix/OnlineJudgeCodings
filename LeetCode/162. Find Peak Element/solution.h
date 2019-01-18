class Solution {
public:
    int helper(vector<int> &nums, int left, int right){
        if(left==right)return left;
        int mid=(left+right)/2;
        if(nums[mid]>nums[mid+1])return helper(nums,left,mid);
        else return helper(nums,mid+1,right);
    }
    int findPeakElement(vector<int>& nums) {
        return helper(nums,0,nums.size()-1);
    }
};