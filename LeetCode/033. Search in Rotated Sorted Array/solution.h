class Solution {
public:
    int search(vector<int>& nums, int target) {
        int mid,left,right,n;
        n=nums.size();left=0;right=n-1;mid=(left+right)/2;
        while(left<=right){
            if(nums[mid]>nums.back())left=mid+1;
            else right=mid-1;
            mid=(left+right)/2;
        }
        right+=n;mid=(left+right)/2;
        while(left<=right){
            if(nums[mid%n]==target)return mid%n;
            else if(nums[mid%n]>target)right=mid-1;
            else left=mid+1;
            mid=(left+right)/2;
        }
        return -1;
    }
};