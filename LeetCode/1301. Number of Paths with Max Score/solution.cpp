using ll = long long;
vector<pair<int,int>> dxy = {{1,0},{0,1},{1,1}};

class Solution {
public:
    vector<int> pathsWithMaxScore(vector<string>& board) {
        const int MOD = 1e9+7;
        int n = board.size(), m = board[0].length();
        board[0][0] = '0'; board[n-1][m-1] = '0';
        vector<vector<int>> score(n+1,vector<int>(m+1,0)), path(n+1,vector<int>(m+1,0));
        path[n-1][m-1] = 1;
        for (int i = n-1; i >= 0; i--){
            for (int j = m-1; j >= 0; j--){
                if (board[i][j] == 'X')
                    continue;
                int mx = 0;
                for (auto [dx,dy] : dxy){
                    dx += i;
                    dy += j;
                    mx = max(mx, score[dx][dy]);
                }
                for (auto [dx,dy] : dxy){
                    dx += i;
                    dy += j;
                    if (mx == score[dx][dy])
                        path[i][j] = ((ll)path[i][j]+path[dx][dy])%MOD;
                }
                score[i][j] = path[i][j] ? mx+board[i][j]-'0' : 0;
            }
        }
        return {score[0][0], path[0][0]};
    }
};