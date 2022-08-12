class Solution {
public:
    int arithmeticTriplets(vector<int>& nums, int diff) {
        set<int>s(nums.begin(),nums.end());
        int ret=0;
        for(int i:s)ret+=(s.count(i-diff)&&s.count(i+diff));
        return ret;
    }
};