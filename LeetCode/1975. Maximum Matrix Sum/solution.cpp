class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        int n = matrix.size(), m = matrix[0].size();
        long long ans = 0, lo = LLONG_MAX, neg = 0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j) {
                ans += abs(matrix[i][j]);
                lo = min(lo, (long long)abs(matrix[i][j]));
                if (matrix[i][j] < 0)
                    neg++;
            }
        if (neg % 2 == 1)
            ans -= lo * 2;
        return ans;
    }
};


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/paT4GG/view/ARvu3X/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。