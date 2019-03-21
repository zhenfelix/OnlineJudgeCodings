class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        int start=0,i=0;
        int n=nums.size();
        vector<string> ans;
        string tmp;
        while(i<n){
            while(i<n-1 && nums[i]+1==nums[i+1])i++;
            tmp=to_string(nums[start]);
            if(i!=start){
                tmp+="->";
                tmp+=to_string(nums[i]);
            }
            ans.push_back(tmp);
            i++;
            start=i;
        }
        return ans;
    }
};