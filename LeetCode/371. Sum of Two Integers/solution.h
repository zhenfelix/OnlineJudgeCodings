class Solution {
public:
    int getSum(int a, int b) {
        if(b==0)return a;
        return getSum(a^b,(a&b)<<1);
    }
};

//https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary:-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently