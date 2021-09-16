vector<pair<int, int>> dxy = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}, {-1, -1}, {1, 1}, {-1,1}, {1,-1}};

class Solution
{
public:
    int flipChess(vector<string> &chessboard)
    {
        int n = chessboard.size(), m = chessboard[0].length();
        int res = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (chessboard[i][j] == '.'){
                    int cnt = bfs(chessboard, i, j);
                    res = max(res, cnt - 1);
                }
                    
            }
        }
        return res;
    }

    int bfs(vector<string> chessboard, int i, int j)
    {
        int n = chessboard.size(), m = chessboard[0].length();
        int cnt = 0;
        queue<pair<int, int>> q;
        q.push({i, j});
        chessboard[i][j] = 'X';
        while (!q.empty())
        {
            auto [r, c] = q.front();
            q.pop();
            cnt++;
            for (auto [dr, dc] : dxy)
            {
                bool flag = true;
                for (int i = r + dr, j = c + dc;; i += dr, j += dc)
                {
                    if (i < 0 || i >= n || j < 0|| j >= m || chessboard[i][j] == '.')
                    {
                        flag = false;
                        break;
                    }
                    if (chessboard[i][j] == 'X')
                        break;
                }
                if (flag)
                {
                    for (int i = r + dr, j = c + dc; i >= 0 && i < n && j >= 0 && j < m && chessboard[i][j] != 'X'; i += dr, j += dc)
                    {

                            q.push({i, j});
                            chessboard[i][j] = 'X';
                    }
                }
            }
        }
        return cnt;
    }
};
