class Solution {
public:
    vector<vector<int>> findFarmland(vector<vector<int>>& land) {
        int n = land.size(), m = land[0].size();
        auto good = [&](int i, int j) {
            if (land[i][j] == 0)  
                return false;
            if (i > 0 && land[i - 1][j] == 1)
                return false;
            if (j > 0 && land[i][j - 1] == 1)
                return false;
            return true;
        };
        vector<vector<int>> ans;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j) {
                if (good(i, j)) {
                    int r = j;
                    while (r + 1 < m && land[i][r + 1] == 1)
                        r++;
                    int d = i;
                    while (d + 1 < n && land[d + 1][j] == 1)
                        d++;
                    ans.push_back({i, j, d, r});
                }
            }
        return ans;
    }
};


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/ZJvAkq/view/Q1VHxC/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。