// class Solution {
// public:
//     void generate(int idx, vector<int> &nums, vector<int> tmp, vector<vector<int>> &ans){
//         if(idx==nums.size()){
//             ans.push_back(tmp);
//             return;
//         }
//         if(!(idx>0&&nums[idx]==nums[idx-1]&&tmp.size()>0&&nums[idx]==tmp.back())){
//             generate(idx+1,nums,tmp,ans);
//             tmp.push_back(nums[idx]);
//             generate(idx+1,nums,tmp,ans);
//         }
//         else{
//             tmp.push_back(nums[idx]);
//             generate(idx+1,nums,tmp,ans);
//         }
//         return;
//     }
//     vector<vector<int>> subsetsWithDup(vector<int>& nums) {
//         sort(nums.begin(),nums.end());
//         vector<vector<int>> ans;
//         vector<int> tmp;
//         generate(0,nums,tmp,ans);
//         return ans;
//     }
// };


class Solution{
  public:
    void generate(vector<vector<int>> &ans, vector<int> nums, vector<int> tmp, int idx){
        // if(idx==nums.size()){
        //     ans.push_back(tmp);
        //     return;
        // }
        ans.push_back(tmp);
        for(int i=idx;i<nums.size();i++){
            if(i>idx&&nums[i]==nums[i-1])continue;
            tmp.push_back(nums[i]);
            generate(ans,nums,tmp,i+1);
            tmp.pop_back();
        }
        return;
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums){
        vector<vector<int>> ans;
        vector<int> tmp;
        sort(nums.begin(),nums.end());
        generate(ans,nums,tmp,0);
        return ans;
    }
};
