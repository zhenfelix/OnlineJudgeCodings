class Solution {
public:
    int largestSubmatrix(vector<vector<int>>& matrix) {
        int n = matrix.size(), m = matrix[0].size(), res = 0;
        vector<int> cc(m,0);
        for (int i = 0; i < n; i++){
            vector<int> height;
            for (int j = 0; j < m; j++){
                cc[j] = matrix[i][j] == 0 ? 0 : cc[j]+1;
                height.push_back(cc[j]);
            }
            sort(height.begin(), height.end(), greater<>());
            int h = n;
            for (int j = 0; j < m && height[j] > 0; j++){
                h = min(h, height[j]);
                res = max(res, h*(j+1));
            }
        }
        return res;
    }
};