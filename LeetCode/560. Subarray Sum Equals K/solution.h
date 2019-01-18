// class Solution {
// public:
//     int subarraySum(vector<int>& nums, int k) {
//         vector<int> sums;
//         sums.push_back(0);
//         for(auto x: nums)sums.push_back(sums.back()+x);
//         int n=sums.size(),ans=0;
//         for(int i=1;i<n;i++){
//             for(int j=0;j<i;j++)if(sums[i]-sums[j]==k)ans++;
//         }
//         return ans;
//     }
// };


class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int sums=0,ans=0;
        unordered_map<int, int> cc;cc[0]=1;
        for(auto x: nums){
            sums+=x;
            ans+=cc[sums-k];
            cc[sums]++;
        }
        return ans;
    }
};