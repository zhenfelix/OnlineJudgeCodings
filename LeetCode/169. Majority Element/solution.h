class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int ans=nums[0];
        int cc=0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]!=ans){
                if(cc<=0){
                    ans=nums[i];
                    cc++;
                }
                else cc--;
            }
            else cc++;
        }
        return ans;
    }
};