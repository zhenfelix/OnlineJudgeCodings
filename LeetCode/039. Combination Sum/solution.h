// class Solution {
// public:
//     void helper(vector<vector<int>> &ans, vector<int> &tmp ,int sum, vector<int> nums, int target){
//         if(sum>target)return;
//         if(sum==target){
//             ans.push_back(tmp);
//             return;
//         }
//         for(int i=0;i<nums.size();i++){
//             if(tmp.size()>0&&nums[i]<tmp.back())continue;
//             tmp.push_back(nums[i]);sum+=nums[i];
//             helper(ans,tmp,sum,nums,target);
//             tmp.pop_back();sum-=nums[i];
//         }
//         return;
//     }
//     vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
//         sort(candidates.begin(),candidates.end());
//         vector<vector<int>> ans;
//         vector<int> tmp;
//         helper(ans,tmp,0,candidates,target);
//         return ans;
//     }
// };

class Solution {
public:
    void helper(vector<vector<int>> &ans, vector<int> &tmp ,int start, vector<int> nums, int target){
        if(target<0)return;
        if(0==target){
            ans.push_back(tmp);
            return;
        }
        for(int i=start;i<nums.size();i++){
            // if(tmp.size()>0&&nums[i]<tmp.back())continue;
            tmp.push_back(nums[i]);target-=nums[i];
            helper(ans,tmp,i,nums,target);
            tmp.pop_back();target+=nums[i];
        }
        return;
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        // sort(candidates.begin(),candidates.end());
        vector<vector<int>> ans;
        vector<int> tmp;
        helper(ans,tmp,0,candidates,target);
        return ans;
    }
};