class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        std::vector<int> res;
        for(auto x: nums){
            x = abs(x);
            if(nums[x-1]<0)res.push_back(x);
            nums[x-1] *= (-1);
        }
        return res;
    }
};