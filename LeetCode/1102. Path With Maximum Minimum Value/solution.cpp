using tiii = tuple<int,int,int>;
using pii = pair<int,int>;

vector<pii> dxy = {{-1,0},{1,0},{0,-1},{0,1}};

class Solution {
public:
    int maximumMinimumPath(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        vector<vector<bool>> visited(n,vector<bool>(m,false));
        vector<tiii> candidates;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                candidates.push_back({grid[i][j],i,j});
            }
        }
        sort(candidates.begin(), candidates.end(), greater<>());

        vector<int> parent(n*m);
        for (int i = 0; i < n*m; i++)
            parent[i] = i;
        function<int(int)> find = [&](int u){
            if (parent[u] != u)
                parent[u] = find(parent[u]);
            return parent[u];
        };
        auto merge = [&](int u, int v){
            int ru = find(u), rv = find(v);
            if (ru != rv){
                parent[ru] = rv;
                return true;
            }
            return false;
        };
        for (auto [val,r,c] : candidates){
            for (auto [dx,dy] : dxy){
                dx += r; dy += c;
                if (dx >= 0 && dx < n && dy >= 0 && dy < m && visited[dx][dy] && merge(r*m+c,dx*m+dy) && find(0) == find(n*m-1))
                    return val;
            }
            visited[r][c] = true;
        }
        return -1;
    }
};




using tiii = tuple<int,int,int>;
using pii = pair<int,int>;

vector<pii> dxy = {{-1,0},{1,0},{0,-1},{0,1}};

class Solution {
public:
    int maximumMinimumPath(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        auto check = [&](int val){
            if (grid[0][0] < val)
                return false;
            queue<pii> q;
            vector<vector<bool>> visited(n,vector<bool>(m,false));
            q.push({0,0});
            visited[0][0] = true;
            while (!q.empty()){
                auto [r,c] = q.front(); q.pop();
                if (r == n-1 && c == m-1)
                    return true;
                for (auto [dx,dy] : dxy){
                    dx += r; dy += c;
                    if (dx >= 0 && dx < n && dy >= 0 && dy < m && !visited[dx][dy] && grid[dx][dy] >= val){
                        q.push({dx,dy});
                        visited[dx][dy] = true;
                    }
                }
            }
            return false;
        };
        
        int lo = 0, hi = 1e9;
        while (lo <= hi){
            int mid = (lo+hi)/2;
            if (check(mid))
                lo = mid + 1;
            else
                hi = mid - 1;
        }
        return hi;
    }
};