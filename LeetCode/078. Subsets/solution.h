// class Solution {
// public:
//     void generate(vector<vector<int>> &ans, vector<int> nums, vector<int> tmp, int idx){
//         if(idx==nums.size()){
//             ans.push_back(tmp);
//             return;
//         }
//         generate(ans,nums,tmp,idx+1);
//         tmp.push_back(nums[idx]);
//         generate(ans,nums,tmp,idx+1);
//         return;
//     }
//     vector<vector<int>> subsets(vector<int>& nums) {
//         vector<vector<int>> ans;
//         vector<int> tmp;
//         generate(ans,nums,tmp,0);
//         return ans;
//     }
// };

// class Solution{
//   public:
//     void generate(vector<vector<int>> &ans, vector<int> nums, vector<int> tmp, int idx){
//         // if(idx==nums.size()){
//         //     ans.push_back(tmp);
//         //     return;
//         // }
//         ans.push_back(tmp);
//         for(int i=idx;i<nums.size();i++){
//             tmp.push_back(nums[i]);
//             generate(ans,nums,tmp,i+1);
//             tmp.pop_back();
//         }
//         return;
//     }
//     vector<vector<int>> subsets(vector<int>& nums){
//         vector<vector<int>> ans;
//         vector<int> tmp;
//         generate(ans,nums,tmp,0);
//         return ans;
//     }
// };


class Solution{
  public:
    void dfs(vector<vector<int>> &ans, vector<int> &nums, vector<int> &path, int idx){
        ans.push_back(path);
        for(int i=idx;i<nums.size();i++){
            path.push_back(nums[i]);
            dfs(ans,nums,path,i+1);
            path.pop_back();
        }
        return;
    }
    vector<vector<int>> subsets(vector<int> &nums){
        vector<vector<int>> ans;
        vector<int> path;
        dfs(ans,nums,path,0);
        return ans;
    }
};


class Solution{
  public:
    void dfs(vector<vector<int>> &ans, vector<int> &nums, vector<int> &path, int idx){
        if(idx==nums.size()){
            ans.push_back(path);
            return;
        }
        dfs(ans,nums,path,idx+1);
        path.push_back(nums[idx]);
        dfs(ans,nums,path,idx+1);
        path.pop_back();
        return;
    }
    vector<vector<int>> subsets(vector<int> &nums){
        vector<vector<int>> ans;
        vector<int> path;
        dfs(ans,nums,path,0);
        return ans;
    }
};