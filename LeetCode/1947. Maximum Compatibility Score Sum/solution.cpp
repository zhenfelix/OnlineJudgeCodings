class Solution {
public:
    int maxCompatibilitySum(vector<vector<int>>& students, vector<vector<int>>& mentors) {
        int m = students.size(), n = students[0].size();
        vector<vector<int>> points(m, vector<int>(m));
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < m; ++j)
                for (int k = 0; k < n; ++k)
                    points[i][j] += students[i][k] == mentors[j][k];
        
        vector<int> dp(1 << m);
        for (int i = 0; i + 1 < (1 << m); ++i) {
            int idx = __builtin_popcount(i);
            for (int j = 0; j < m; ++j) {
                if (!(i & (1 << j))) {
                    int nxt = i ^ (1 << j);
                    dp[nxt] = max(dp[nxt], dp[i] + points[idx][j]);
                }
            }
        }
        
        return dp.back();
    }
};

