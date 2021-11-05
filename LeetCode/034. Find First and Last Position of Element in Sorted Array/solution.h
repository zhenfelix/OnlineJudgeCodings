class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> res;
        int n = nums.size();
        int lo = 0, hi = n-1;
        while (lo <= hi){
            int mid = (lo+hi)/2;
            if (nums[mid] >= target)
                hi = mid - 1;
            else
                lo = mid + 1;
        }
        if (lo > n-1 || nums[lo] != target)
            return {-1,-1};
        res.push_back(lo);
        lo = 0, hi = n-1;
        while (lo <= hi){
            int mid = (lo+hi)/2;
            if (nums[mid] > target)
                hi = mid - 1;
            else
                lo = mid + 1;
        }
        res.push_back(lo-1);
        return res;
    }
};



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