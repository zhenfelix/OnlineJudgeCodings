class Solution {
public:
    int minOperations(vector<int>& nums) {
        int ones = 0, mul = 0;
        for (auto x : nums){
            for (int i = 0; x > 0; i++){
                ones += (x&1);
                x >>= 1;
                mul = max(mul,i);
            }
        }
        return ones+mul;
    }
};