class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int n=nums.size(),left,right,mid;
        vector<int> ans{-1,-1};
        left=0;right=n-1;mid=(left+right)/2;
        while(left<=right){
            if(nums[mid]<target)left=mid+1;
            else right=mid-1;
            mid=(left+right)/2;
        }
        if((left==n)||(right==-1&&nums[0]!=target))return ans;
        ans[0]=right+1;
        left=0;right=n-1;mid=(left+right)/2;
        while(left<=right){
            if(nums[mid]>target)right=mid-1;
            else left=mid+1;
            mid=(left+right)/2;
        }
        if((right==-1)||(left==n&&nums[n-1]!=target))return ans;
        ans[1]=left-1;
        if(ans[0]>ans[1])ans[0]=-1,ans[1]=-1;
        return ans;
    }
};