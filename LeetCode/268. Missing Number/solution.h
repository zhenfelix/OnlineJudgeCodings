class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int len=nums.size();
        int a=len*(len+1)/2;
        int b=0;
        for(int x: nums)b+=x;
        return a-b;
    }
};