class Solution {
public:
    int lenLongestFibSubseq(vector<int>& arr) {
        int n = arr.size();
        int res = 0;
        vector<vector<int>> dp(n, vector<int>(n,0));
        unordered_map<int,int> mp;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < i; j++){
                if (arr[j] <= arr[i]){
                    if (arr[i]-arr[j] <= arr[j] && mp.count(arr[i]-arr[j])){
                        int k = mp[arr[i]-arr[j]];
                        if (k < j){
                            dp[i][j] = max(dp[i][j], dp[j][k]+1);
                            res = max(res, dp[i][j]+2);
                        }
                    }
                }
            }
            mp[arr[i]] = i;
        }
        return res >= 3 ? res : 0;
    }
};


class Solution {
public:
    int lenLongestFibSubseq(vector<int>& arr) {
        int n = arr.size();
        int res = 0;
        // vector<vector<int>> dp(n, vector<int>(n,0));
        unordered_map<int,int> dp, mp;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < i; j++){
                if (arr[j] <= arr[i]){
                    if (arr[i]-arr[j] <= arr[j] && mp.count(arr[i]-arr[j])){
                        int k = mp[arr[i]-arr[j]];
                        if (k < j){
                            dp[i*n+j] = max(dp[i*n+j], dp[j*n+k]+1);
                            res = max(res, dp[i*n+j]+2);
                        }
                    }
                }
            }
            mp[arr[i]] = i;
        }
        return res >= 3 ? res : 0;
    }
};


// TLE O(N2)
// class Solution {
// public:
//     int lenLongestFibSubseq(vector<int>& arr) {
//         int n = arr.size();
//         int res = 0;
//         vector<unordered_map<int,int>> dp(n);
//         for (int i = 0; i < n; i++){
//             for (int j = 0; j < i; j++){
//                 if (arr[j] <= arr[i]){
//                     if (arr[i]-arr[j] <= arr[j] && dp[j].count(arr[i]-arr[j])){
//                         dp[i][arr[j]] = max(dp[i][arr[j]], dp[j][arr[i]-arr[j]]+1);
//                         res = max(res, dp[i][arr[j]]+2);
//                     }
//                     else{
//                         dp[i][arr[j]] = 0;
//                     }
//                 }
                
//             }
//         }
//         return res >= 3 ? res : 0;
//     }
// };

