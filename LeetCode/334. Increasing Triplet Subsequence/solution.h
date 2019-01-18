class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int first=INT_MAX,second=INT_MAX;
        for(auto x: nums){
            if(x<=first)first=x;
            else if(x<=second)second=x;
            else return true;
        }
        return false;
    }
};