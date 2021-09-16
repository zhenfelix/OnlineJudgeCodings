class Solution {
public:
    vector<int> getMaximumXor(vector<int>& nums, int maximumBit) {
        int sums = accumulate(nums.begin(), nums.end(), 0, [](int a, int b){ return a^b; });
        int total = (1<<maximumBit)-1;
        vector<int> res;
        while(!nums.empty()){
            int tmp = nums.back();
            nums.pop_back();
            res.emplace_back(total^sums);
            sums ^= tmp;
        }
        return res;
    }
};


class Solution {
public:
    vector<int> getMaximumXor(vector<int>& nums, int maximumBit) {
        int mask = (1<<maximumBit)-1;
        int cur = accumulate(nums.begin(), nums.end(), 0, [](int a, int b){
            return a^b;
        });
        vector<int> ans;
        while (!nums.empty()){
            ans.push_back(mask^cur);
            cur ^= nums.back(); nums.pop_back();
        }
        return ans;
    }
};