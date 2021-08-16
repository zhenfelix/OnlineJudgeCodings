const int d[8][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
const int n = 8;

class Solution {
public:
    bool checkMove(vector<vector<char>>& board, int r, int c, char color) {
        int bw = 'B' + 'W';
        auto valid = [&](int i, int j) {
            return i >= 0 && i < n && j >= 0 && j < n;
        };
        
        for (int k = 0; k < 8; ++k) {
            int nr = r + d[k][0], nc = c + d[k][1];
            int len = 0;
            while (valid(nr, nc) && board[nr][nc] + color == bw) {
                len++, nr += d[k][0], nc += d[k][1];
            }
            if (valid(nr, nc) && board[nr][nc] == color && len > 0)
                return true;
        }
        return false;
    }
};


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/9suuWs/view/8lA5Vo/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。