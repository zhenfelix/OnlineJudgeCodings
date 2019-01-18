// class Solution {
// public:
//     int longestConsecutive(vector<int>& nums) {
//         int ans=0,tmp=1;
//         sort(nums.begin(),nums.end());
//         for(int i=0;i<nums.size();i++){
//             if(i<(nums.size()-1)&&nums[i+1]==nums[i]+1)tmp++;
//             else if(i<(nums.size()-1)&&nums[i+1]==nums[i])continue;
//             else{
//                 if(tmp>ans)ans=tmp;
//                 tmp=1;
//             }
//         }
//         return ans;
//     }
// };

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s;
        int ans=0,tmp;
        for(auto x: nums)s.insert(x);
        for(auto x: nums){
            if(s.find(x-1)==s.end()){
                tmp=0;
                while(s.find(x)!=s.end()){
                    x++;
                    tmp++;
                }
                ans=max(ans,tmp);
            }
        }
        return ans;
    }
};