vector<pair<int,int>> dxy = {{-1,0},{1,0},{0,-1},{0,1}};

class Solution {
public:
    int dfs(int i, int j, vector<vector<int>> &visited){
        int cnt = 1, n = visited.size(), m = visited[0].size();
        visited[i][j] = 0;
        for (auto [dx,dy] : dxy){
            dx += i;
            dy += j;
            if (dx >= 0 && dx < n && dy >= 0 && dy < m && visited[dx][dy] == 1)
                cnt += dfs(dx,dy,visited);
        }
        return cnt;
    }
    bool check(vector<vector<int>> &visited){
        int tot = 0, n = visited.size(), m = visited[0].size();
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (visited[i][j]){
                    if (tot)
                        return false;
                    tot += dfs(i,j,visited);
                }
            }
        }
        return tot>0;
    }
    int minDays(vector<vector<int>>& grid) {
        vector<vector<int>> visited = grid;
        int n = visited.size(), m = visited[0].size();
        if(!check(visited))
            return 0;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (grid[i][j] == 1){
                    visited = grid;
                    visited[i][j] = 0;
                    if (!check(visited))
                        return 1;
                }
            }
        }
        return 2;

    }
};














vector<pair<int,int>> dxy = {{-1,0},{1,0},{0,-1},{0,1}};

class Solution {
    vector<int> low, tin;
    int clock, n, m;
    bool found = false;
public:
    void tarjan(int cur, int parent, vector<vector<int>> &grid){
        int i = cur/m, j = cur%m, pi = parent/m, pj = parent%m;
        low[cur] = tin[cur] = clock++;
        for (auto [dx,dy] : dxy){
            dx += i;
            dy += j;
            if (dx < 0 || dx >= n || dy < 0 || dy >= m || grid[dx][dy] == 0)
                continue;
            int nxt = dx*m+dy;
            if (nxt == parent)
                continue;
            else if (tin[nxt] != -1){
                low[cur] = min(low[cur], tin[nxt]);
            }
            else{
                tarjan(nxt,cur,grid);
                low[cur] = min(low[cur], low[nxt]);
                if (low[nxt] > tin[cur])
                    found = true;
            }
        }
        // cout << i << " " << j << " " << child << endl;
        return;
    }
    int dfs(int i, int j, vector<vector<int>> &visited){
        int cnt = 1;
        visited[i][j] = 0;
        for (auto [dx,dy] : dxy){
            dx += i;
            dy += j;
            if (dx >= 0 && dx < n && dy >= 0 && dy < m && visited[dx][dy] == 1)
                cnt += dfs(dx,dy,visited);
        }
        return cnt;
    }
    bool check(vector<vector<int>> &visited){
        int tot = 0;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (visited[i][j]){
                    if (tot)
                        return false;
                    tot += dfs(i,j,visited);
                }
            }
        }
        return tot>0;
    }
    int minDays(vector<vector<int>>& grid) {
        vector<vector<int>> visited = grid;
        n = visited.size(), m = visited[0].size();
        if(!check(visited))
            return 0;
        clock = 0;
        tin.assign(n*m,-1);
        low.assign(n*m,-1);
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (grid[i][j] == 1){
                    tarjan(i*m+j,-1,grid);
                    // cout << clock << endl;
                    if (clock == 1 || (clock > 2 && found))
                        return 1;
                    return 2;
                }
            }
        }
        return 2;

    }
};