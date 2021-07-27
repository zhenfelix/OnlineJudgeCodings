const int inf = 0x3f3f3f3f;
const int ninf = -inf;

class Solution {
public:
    long long maxPoints(vector<vector<int>>& points) {
        vector<long long> dp(points[0].begin(), points[0].end());
        int n = points.size(), m = points[0].size();
        for (int i = 1; i < n; i++){
            vector<long long> ndp(m, ninf);
            long long mx = ninf;
            for (int j = 0; j < m; j++){
                mx = max(mx, dp[j]+j);
                ndp[j] = max(ndp[j], mx-j+points[i][j]);
            }
            mx = ninf;
            for (int j = m-1; j >= 0; j--){
                mx = max(mx, dp[j]-j);
                ndp[j] = max(ndp[j], mx+j+points[i][j]);
            }
            std:swap(dp, ndp);
        }
        return *max_element(dp.begin(), dp.end());
        
    }
};