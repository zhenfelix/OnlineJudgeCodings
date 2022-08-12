class Solution {
    const int P = 1000007;
    const int MOD = 998244353;

public:
    int equalPairs(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<long long> R(n), C(n);
        for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) R[i] = (R[i] * P + grid[i][j]) % MOD;
        for (int j = 0; j < n; j++) for (int i = 0; i < n; i++) C[j] = (C[j] * P + grid[i][j]) % MOD;

        int ans = 0;
        for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) if (R[i] == C[j]) ans++;
        return ans;
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/sWfXxC/view/gEN00n/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。