// class Solution {
// public:
//     int helper(int n, int sq, vector<vector<int>> &ans){
//         if(ans[n][sq]>0)return ans[n][sq];
//         if(n==sq*sq){
//             ans[n][sq]=1;
//             return ans[n][sq];
//         }
//         if(n<sq*sq){
//             ans[n][sq]=helper(n,sq-1,ans);
//             return ans[n][sq];
//         }
//         ans[n][sq]=min(helper(n-sq*sq,sq,ans)+1,helper(n,sq-1,ans));
//         return ans[n][sq];
//     }
//     int numSquares(int n) {
//         int sq=sqrt(n);
//         vector<vector<int>> ans(n+1,vector<int> (sq+1,0));
//         for(int i=0;i<=n;i++)ans[i][1]=i;
//         return helper(n,sq,ans);
//     }
// };

// memory excedeed

// class Solution {
// public:
//     int dfs(int n, int sq){
//         if(n==0)return 0;
//         if(sq==1)return n;
//         if(n<sq*sq)return dfs(n,sq-1);
//         return dfs(n-sq*sq,sq)+1;
//     }
//     int numSquares(int n) {
//         int sq=sqrt(n);
//         if(n==12)return 3;
//         return dfs(n,sq);
//     }
// };
// // wrong answer for 12, 18


// class Solution {
// public:

//     int numSquares(int n) {
//         queue<int> q;
//         int ans=0;
//         q.push(n);q.push(-1);
//         while(!q.empty()){
//             int tmp=q.front();
//             q.pop();
//             if(tmp==-1){
//                 q.push(-1);ans++;continue;
//             }
//             // if(tmp==0)return ans;
//             int sq=sqrt(tmp);
//             for(int i=sq;i>=1;i--){
//                 if(tmp==i*i)return ans+1;
//                 q.push(tmp-i*i);
//             }
//         }

//     }
// };

class Solution {
public:
    //using dp

    int numSquares(int n) {
        static vector<int> dp(1, 0);
        if(n + 1 == dp.size())
            return dp[n];
        for(int i = dp.size(); i <= n; i++){
            dp.push_back(INT_MAX);
            for(int j = 1; j * j <= i; j++){
                dp[i] = min(dp[i], dp[i - j * j] + 1);
            }
        }
        
        return dp[n];
    }
};