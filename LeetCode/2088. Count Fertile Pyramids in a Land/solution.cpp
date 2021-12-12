class Solution {
    int count(vector<vector<int>> &grid) {
        int n = grid.size(), m = grid[0].size();
        vector<int> dp(m + 2); // 在首尾各增加了一个哨兵位，以避免对边界情况的讨论。
        
        int ans = 0;
        for (int i = n - 1; i >= 0; --i) {
            vector<int> ndp(m + 2);
            for (int j = 0; j < m; ++j) {
                if (grid[i][j] == 0)
                    continue;
                
                ndp[j + 1] = min(dp[j], min(dp[j + 1], dp[j + 2])) + 1;
                ans += ndp[j + 1] - 1;
            }
            dp = move(ndp); // 滚动数组
        }
        
        return ans;
    }
    
public:
    int countPyramids(vector<vector<int>>& grid) {
        int ans = count(grid);
        reverse(grid.begin(), grid.end());
        ans += count(grid);
        
        return ans;
    }
};


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/jPIdc4/view/8u6s2V/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。