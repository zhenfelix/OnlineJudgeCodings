class Solution {
public:
    int arraySign(vector<int>& nums) {
        int cur = 1;
        for (auto &x: nums)
        {
            int tmp = x >= 0 ? (x > 0 ? 1: 0) : -1;
            cur *= tmp;
        }
        return cur;
    }
};