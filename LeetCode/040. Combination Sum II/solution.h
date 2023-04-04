

// class Solution {
// public:
//     void helper(vector<vector<int>> &ans, vector<int> &tmp ,int start, vector<int> nums, int target, vector<bool> used){
//         if(target<0)return;
//         if(0==target){
//             ans.push_back(tmp);
//             return;
//         }
//         for(int i=start;i<nums.size();i++){
//             if(i>0&&nums[i]==nums[i-1]&&!used[i-1])continue;
//             tmp.push_back(nums[i]);target-=nums[i];used[i]=true;
//             helper(ans,tmp,i+1,nums,target,used);
//             tmp.pop_back();target+=nums[i];used[i]=false;
//         }
//         return;
//     }
//     vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
//         sort(candidates.begin(),candidates.end());
//         vector<vector<int>> ans;
//         vector<int> tmp;
//         vector<bool> used(candidates.size(),false);
//         helper(ans,tmp,0,candidates,target,used);
//         return ans;
//     }
// };


class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        sort(candidates.begin(), candidates.end(), greater<>{});
        int n = candidates.size();
        function<void(int, vector<int>&, int)> dfs = [&](int i, vector<int>& path, int s){
            
            if (s > target) return;
            if (i == n){
                if (s == target){
                ans.push_back(path);
            }
            return;
            }
            if (path.empty() || path.back() != candidates[i])
                dfs(i+1,path,s);
            path.push_back(candidates[i]);
            s += candidates[i];
            dfs(i+1,path,s);
            path.pop_back();
            return;
        };
        vector<int> path;
        dfs(0,path,0);
        return ans;

    }
};

class Solution {
public:
    void helper(vector<vector<int>> &ans, vector<int> &tmp ,int start, vector<int> &nums, int target){
        if(target<0)return;
        if(0==target){
            ans.push_back(tmp);
            return;
        }
        for(int i=start;i<nums.size();i++){
            if(i>start&&nums[i]==nums[i-1])continue;
            tmp.push_back(nums[i]);target-=nums[i];
            helper(ans,tmp,i+1,nums,target);
            tmp.pop_back();target+=nums[i];
        }
        return;
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(),candidates.end());
        vector<vector<int>> ans;
        vector<int> tmp;
        helper(ans,tmp,0,candidates,target);
        return ans;
    }
};