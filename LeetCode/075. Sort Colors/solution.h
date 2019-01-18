class Solution {
public:
    void sortColors(vector<int>& nums) {
        int start=0,end=nums.size()-1;
        for(int i=0;i<=end;){
            if(nums[i]==0){
                swap(nums[i],nums[start]);
                start++,i++;
            }
            else if(nums[i]==1)i++;
            else{
                swap(nums[i],nums[end]);
                end--;
            }
        }
    }
};