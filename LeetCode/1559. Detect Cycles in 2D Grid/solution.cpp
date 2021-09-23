using pp = pair<int,int>;

vector<pp> dxy = {{-1,0},{1,0},{0,-1},{0,1}};

class Solution {
public:
    int n, m;
    vector<vector<bool>> visited;
    vector<vector<char>> grid;
    bool tarjan(int i, int j, int pi, int pj){
        visited[i][j] = true;
        for (auto [dx,dy] : dxy){
            dx += i; dy += j;
            if (dx == pi && dy == pj)
                continue;
            if (dx < 0 || dx >= n || dy < 0 || dy >= m)
                continue;
            if (grid[i][j] != grid[dx][dy])
                continue;
            if (visited[dx][dy]){
                // cout << i << " " << j << " " << pi << " " << pj << " " << dx << " " << dy << endl;
                return true;
            }
                
            if (tarjan(dx,dy,i,j))
                return true;
        }
        return false;
    }
    bool containsCycle(vector<vector<char>>& grid) {
        this->grid = grid;
        n = grid.size(), m = grid[0].size();
        visited.resize(n);
        for (int i = 0; i < n; i++)
            visited[i].assign(m,false);
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (!visited[i][j] && tarjan(i,j,-1,-1))
                    return true;
            }
        }
        return false;
    }
};