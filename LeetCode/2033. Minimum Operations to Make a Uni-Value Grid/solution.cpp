class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        int n = grid.size(), m = grid[0].size(), mod = grid[0][0] % x;
        vector<int> v;
        for (auto &row : grid)
            for (int cell : row) {
                if (cell % x != mod)
                    return -1;
                v.emplace_back(cell / x);
            }
        int mid = n * m / 2;
        nth_element(v.begin(), v.begin() + mid, v.end());
        int ans = 0;
        for (int vi : v)
            ans += abs(vi - v[mid]);
        return ans;
    }
};


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/2ELXyY/view/DxDKIC/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。