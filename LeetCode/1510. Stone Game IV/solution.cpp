const int maxn = 1e5+5;

bool dp[maxn];

class Solution {
public:
    bool winnerSquareGame(int n) {
     dp[0] = false;
     for (int i = 1; i <= n; i++){
         dp[i] = false;
         for (int j = 1; j*j <= i; j++){
             if (!dp[i-j*j]){
                 dp[i] = true;
                 break;
             }
         }
     }
     return dp[n];
    }
};

// const int maxn = 1e5+5;

// bitset<maxn> dp;

// class Solution {
// public:
//     bool winnerSquareGame(int n) {
//         dp[0] = 0;
//         for (int i = 1; i <= n; i++){
//             dp[i] = 0;
//             for (int j = 1; j*j <= i; j++){
//                 if (!dp[i-j*j]){
//                     dp[i] = 1;
//                     break;
//                 }
//             }
//         }
//         return dp[n];
//     }
// };