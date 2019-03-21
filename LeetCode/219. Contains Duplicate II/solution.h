// class Solution {
// public:
//     bool containsNearbyDuplicate(vector<int>& nums, int k) {
//         int n=nums.size();
//         for(int i=0;i<n;i++){
//             for(int j=1;j<=k && i+j<n;j++){
//                 if(nums[i]==nums[i+j])return true;
//             }
//         }
//         return false;
//     }
// };


class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        int n=nums.size();
        for(int i=0;i<n;i++){
            int x=nums[i];
            if(mp.find(x)==mp.end()){mp[x]=i;}
            else{
                if(i-mp[x]<=k)return true;
                else mp[x]=i;
            }
        }
        return false;
    }
};