// const int inf = 0x3f3f3f3f;

// class Solution {
// public:
//     bool oneEditAway(string first, string second) {
//         int n = first.size(), m = second.size();
//         vector<vector<int>> dp(n+1, vector<int>(m+1, inf));
//         dp[0][0] = 0;
//         for (int i = 1; i <= n; i++)
//             dp[i][0] = dp[i-1][0] + 1;
//         for (int j = 1; j <= m; j++)
//             dp[0][j] = dp[0][j-1] + 1;
//         for (int i = 1; i <= n; i++){
//             for (int j = 1; j <= m; j++){
//                 dp[i][j] = (first[i-1] == second[j-1] ? 0 : 1) + dp[i-1][j-1];
//                 dp[i][j] = min(dp[i][j], dp[i][j-1]+1);
//                 dp[i][j] = min(dp[i][j], dp[i-1][j]+1);
//             }
//         }
//         return dp[n][m] <= 1;
//     }
// };


class Solution {
public:
    bool oneEditAway(string first, string second) {
        int n = first.size(), m = second.size();
        vector<int> dp(m+1, 0), ndp(m+1, 0);
        
        for (int j = 1; j <= m; j++)
            dp[j] = dp[j-1] + 1;
        for (int i = 1; i <= n; i++){
            ndp[0] = dp[0] + 1;
            for (int j = 1; j <= m; j++){
                ndp[j] = (first[i-1] == second[j-1] ? 0 : 1) + dp[j-1];
                ndp[j] = min(ndp[j], ndp[j-1]+1);
                ndp[j] = min(ndp[j], dp[j]+1);
            }
            std::swap(dp, ndp);
        }
        return dp[m] <= 1;
    }
};

class Solution {
public:
    bool oneEditAway(string first, string second) {
        int n = first.size(), m = second.size();
        if (n > m){
            std::swap(first, second);
            std::swap(n, m);
        }
            
        if (m - n > 1)
            return false;
        int a = 0, b = 1;
        for (int i = 1; i <= n; i++){
            int aa = min(a+(first[i-1] == second[i-1] ? 0 : 1), b+1);
            a = aa;
            if (i <= m)
            {
                int bb = min(aa+1, b+(first[i-1] == second[i] ? 0 : 1));
                b = bb;
            }            
        }
        if (n == m)
            return a <= 1;
        return b <= 1;
    }
};


class Solution {
public:
    bool oneEditAway(string first, string second) {
        int n = first.size(), m = second.size();
        if (n > m){
            return oneEditAway(second, first);
        }
        if (m - n > 1)
            return false;
        for (int i = 0; i < n; i++){
            if (first[i] != second[i])
                return first.substr(i+(n!=m?0:1)) == second.substr(i+1);
        }
       
        return true;
    }
};