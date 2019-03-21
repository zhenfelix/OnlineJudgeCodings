// class Solution {
// public:
//     int triangleNumber(vector<int>& nums) {
//         int ans=0;
//         sort(nums.begin(),nums.end());
//         for(int i=0;i<nums.size()-1;i++){
//             for(int j=i+1;j<nums.size();j++){
//                 int tmp=lower_bound(nums.begin(),nums.end(),nums[i]+nums[j])-nums.begin()-1-j;
//                 ans+=max(0,tmp);
//             }
//         }
//         return ans;
//     }
// };

class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int ans=0, n=nums.size();
        sort(nums.begin(),nums.end());
        for(int i=0;i<n-2;i++){
            int k=i+2;
            for(int j=i+1;j<n-1&&nums[i]>0;j++){
                while(k<n && nums[i]+nums[j]>nums[k])k++;
                ans+=k-1-j;
            }
        }
        return ans;
    }
};

//try int n=nums.size(); because nums.size()type is unsigned int, and nums.size()-2 will be a large positive number if nums.size()==1