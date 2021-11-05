// class Solution {
// public:
//     int candy(vector<int>& ratings) {
//         int n = ratings.size();
//         vector<int> idx;
//         for (int i = 0; i < n; i++)
//             idx.push_back(i);
//         sort(idx.begin(), idx.end(), [&](int a, int b){
//             return ratings[a] < ratings[b];
//         });
//         vector<int> dp(n,1);
//         for (auto i : idx){
//             if (i-1 >= 0 && ratings[i-1] < ratings[i])
//                 dp[i] = max(dp[i], dp[i-1]+1);
//             if (i+1 < n && ratings[i+1] < ratings[i])
//                 dp[i] = max(dp[i], dp[i+1]+1);
//         }
//         return accumulate(dp.begin(), dp.end(), 0);
//     }
// };


// class Solution {
// public:
//     int candy(vector<int>& ratings) {
//         int n = ratings.size();
//         vector<int> dp(n,1);
//         function<int(int,int)> dfs = [&](int left, int right){
//             if (left > right)
//                 return 0;
//             int k = max_element(ratings.begin()+left, ratings.begin()+right+1)-ratings.begin();
//             int lsums = dfs(left,k-1), rsums = dfs(k+1,right);
//             if (k-1 >= 0 && ratings[k-1] < ratings[k])
//                 dp[k] = max(dp[k], dp[k-1]+1);
//             if (k+1 < n && ratings[k+1] < ratings[k])
//                 dp[k] = max(dp[k], dp[k+1]+1);
//             // cout << left << " " << right << " " << k << " " << ratings[k] << " " << dp[k] << " " << lsums << " " << rsums << endl;
//             return dp[k]+lsums+rsums;
//         };
//         return dfs(0,n-1);
//     }
// };


// class Solution {
// public:
//     int candy(vector<int>& ratings) {
//         int n = ratings.size();
//         vector<int> dp(n,1);
//         function<int(int,int)> dfs = [&](int left, int right){
//             if (left > right)
//                 return 0;
//             int k = right;
//             for (int kk = left; kk < right; kk++){
//                 if (ratings[kk] > ratings[k])
//                     k = kk;
//             }
//             int lsums = dfs(left,k-1), rsums = dfs(k+1,right);
//             if (k-1 >= 0 && ratings[k-1] < ratings[k])
//                 dp[k] = max(dp[k], dp[k-1]+1);
//             if (k+1 < n && ratings[k+1] < ratings[k])
//                 dp[k] = max(dp[k], dp[k+1]+1);
//             // cout << left << " " << right << " " << k << " " << ratings[k] << " " << dp[k] << " " << lsums << " " << rsums << endl;
//             return dp[k]+lsums+rsums;
//         };
//         return dfs(0,n-1);
//     }
// };

const int inf = 0x3f3f3f3f;
class Solution {
public:
    int candy(vector<int>& ratings) {
        ratings.push_back(inf);
        int n = ratings.size();
        vector<int> dp(n,1), st;
        int sums = 0;
        for (int i = 0; i < n; i++){
            while (!st.empty() && ratings[st.back()] < ratings[i]){
                int j = st.back(); st.pop_back();
                if (j-1 >= 0 && ratings[j-1] < ratings[j])
                    dp[j] = max(dp[j], dp[j-1]+1);
                if (j+1 < n && ratings[j+1] < ratings[j])
                    dp[j] = max(dp[j], dp[j+1]+1);
                sums += dp[j];
            }
            st.push_back(i);
        }
        return sums;
    }
};