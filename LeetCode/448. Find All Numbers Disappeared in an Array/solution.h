// class Solution {
// public:
//     vector<int> findDisappearedNumbers(vector<int>& nums) {
//         int len = nums.size();
//         for(int i=0; i<len; i++) {
//             int m = abs(nums[i])-1; // index start from 0
//             nums[m] = nums[m]>0 ? -nums[m] : nums[m];
//         }
//         vector<int> res;
//         for(int i = 0; i<len; i++) {
//             if(nums[i] > 0) res.push_back(i+1);
//         }
//         return nums;
//     }
// };

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int len = nums.size();
        vector<int> vote(len,0);
        for(int i=0; i<len; i++)if(!vote[nums[i]-1])vote[nums[i]-1]=1;
        vector<int> res;
        for(int i = 0; i<len; i++)if(!vote[i])res.push_back(i+1);
        return res;
    }
};