My elegant recursive single permutation solution
```c++
class Solution {
public:
    void generate(int idx, vector<int> &nums, int n, vector<vector<int>> &ans){
        if(idx==n)ans.push_back(nums);
        for(int i=idx;i<n;i++){
            swap(nums[idx],nums[i]);
            generate(idx+1,nums,n,ans);
            swap(nums[idx],nums[i]);
        }
        return;
    }
    vector<vector<int>> permute(vector<int>& nums) {
        int n=nums.size();
        vector<vector<int>> ans;
        generate(0,nums,n,ans);
        return ans;
    }
};
```
