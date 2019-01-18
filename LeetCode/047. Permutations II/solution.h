// class Solution {
// public:
//     vector<vector<int>> permuteUnique(vector<int>& nums) {
//         vector<vector<int>> ans;
//         vector<int> tmp;
//         vector<bool> used(nums.size(),false);
//         // unordered_map<int,bool> used(nums.size(),false);
//         sort(nums.begin(),nums.end());
//         helper(ans,tmp,used,nums);
//         return ans;
//     }
//     void helper(vector<vector<int>> &ans, vector<int> &tmp, vector<bool> &used, vector<int> nums){
//         if(tmp.size()==nums.size()){
//             ans.push_back(tmp);
//             return;
//         }
//         for(int i=0;i<nums.size();i++){
//             if(used[i])continue;
//             if(i>0&&nums[i]==nums[i-1]&&!used[i-1])continue;
//             used[i]=true;
//             tmp.push_back(nums[i]);
//             helper(ans,tmp,used,nums);
//             tmp.pop_back();
//             used[i]=false;
//         }
//         return;
//     }
// };



// class Solution {
// public:
//     vector<vector<int>> permuteUnique(vector<int>& nums) {
//         vector<vector<int>> result;
//         // sort(nums.begin(), nums.end());
//         permuteUniqueHelper(nums, 0, result);
//         return result;
//     }
    
//     void permuteUniqueHelper(vector<int>& nums, int start, vector<vector<int>>& result) {
//         if (start >= nums.size()) {
//             result.push_back(nums);
//             return;
//         }
//         unordered_set<int> s;
//         for (int i = start; i < nums.size(); i++) {
//             if (s.find(nums[i]) != s.end()) {
//                 continue;
//             }
//             s.insert(nums[i]);
//             swap(nums[i], nums[start]);
//             permuteUniqueHelper(nums, start + 1, result);
//             swap(nums[i], nums[start]);
//         }
//     }
// };



class Solution {
public:
    void recursion(vector<int> num, int i, int j, vector<vector<int> > &res) {
        if (i == j-1) {
            res.push_back(num);
            return;
        }
        for (int k = i; k < j; k++) {
            if (i != k && num[i] == num[k]) continue;
            swap(num[i], num[k]);
            recursion(num, i+1, j, res);
        }
    }
    vector<vector<int> > permuteUnique(vector<int> &num) {
        sort(num.begin(), num.end());
        vector<vector<int> >res;
        recursion(num, 0, num.size(), res);
        return res;
    }
};