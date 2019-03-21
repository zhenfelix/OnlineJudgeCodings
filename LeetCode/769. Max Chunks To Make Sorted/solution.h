// class Solution {
// public:
//     int maxChunksToSorted(vector<int>& arr) {
//         int reach=-1;
//         int n=arr.size();
//         int ans=0;
//         for(int i=0;i<n;i++){
//             if(i>reach){
//                 reach=arr[i];
//                 ans++;
//             }
//             else{
//                 reach=max(reach,arr[i]);
//             }
//         }
//         return ans;
//     }
// };

class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int n=arr.size();
        vector<int> dp(n,-1);
        int ans=0;
        dp[0]=arr[0];
        for(int i=1;i<n;i++){
            dp[i]=max(dp[i-1],arr[i]);
        }
        for(int i=0;i<n;i++)if(dp[i]==i)ans++;
        return ans;
    }
};