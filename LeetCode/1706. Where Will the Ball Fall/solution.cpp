class Solution {
public: vector<int> findBall(vector<vector<int>> &grid) {
        int row = grid.size();
        int col = grid[0].size();
        vector<int> ans(col);

        // 默认位置
        for (int i = 0; i < col; i++) {
            ans[i] = i;
        }

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (ans[j] == -1) {//忽略卡住的球
                    continue;
                }
                if (grid[i][ans[j]] == 1 && ans[j] + 1 < col && grid[i][ans[j] + 1] == 1) {
                    //右移
                    ans[j]++;
                } else if (grid[i][ans[j]] == -1 && ans[j] - 1 >= 0 && grid[i][ans[j] - 1] == -1) {
                    //左移
                    ans[j]--;
                } else {
                    //卡住
                    ans[j] = -1;
                }
            }
        }
        return ans;
    }
};


// 作者：Ethan-JX
// 链接：https://leetcode-cn.com/problems/where-will-the-ball-fall/solution/java-shuang-bai-di-gui-by-ethan-jx-yvx6/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。