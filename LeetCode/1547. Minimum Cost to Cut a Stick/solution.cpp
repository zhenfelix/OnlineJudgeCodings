const int inf = 0x3f3f3f3f;

class Solution {
public:
    int minCost(int n, vector<int>& cuts) {
        cuts.push_back(0);
        cuts.push_back(n);
        sort(cuts.begin(), cuts.end());
        int m = cuts.size();
        vector<vector<int>> dp(m, vector(m,inf));
        for (int i = m-1; i >= 0; i--){
            if (i+1 < m)
                dp[i][i+1] = 0;
            for (int j = i+2; j < m; j++){
                for (int k = i+1; k < j; k++)
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j]+cuts[j]-cuts[i]);
            }
        }
        return dp[0][m-1];
    }
};



const int inf = 0x3f3f3f3f;
const int maxn = 105;
int dp[maxn][maxn];

class Solution {
public:
    int minCost(int n, vector<int>& cuts) {
        cuts.push_back(0);
        cuts.push_back(n);
        sort(cuts.begin(), cuts.end());
        int m = cuts.size();
        for (int i = m-1; i >= 0; i--){
            for (int j = i+1; j < m; j++){
                if (j == i+1)
                    dp[i][j] = 0;
                else
                    dp[i][j] = inf;
                for (int k = i+1; k < j; k++)
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j]+cuts[j]-cuts[i]);
            }
        }
        return dp[0][m-1];
    }
};
