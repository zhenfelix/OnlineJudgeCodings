// using tiii = tuple<int,int,int>;
// const int inf = 0x3f3f3f3f;

// class Solution {
// public:
//     int minCost(vector<vector<int>>& grid) {
//         int n = grid.size(), m = grid[0].size();
//         vector<pair<int,int>> dxy = {{0,1},{0,-1},{1,0},{-1,0}};
//         vector<vector<int>> dp(n,vector<int>(m,inf));
//         dp[0][0] = 0;
//         priority_queue<tiii,vector<tiii>,greater<>> pq;
//         pq.push({0,0,0});
//         while (!pq.empty()){
//             auto [cost, i, j] = pq.top(); pq.pop();
//             if (i == n-1 && j == m-1)
//                 return cost;
//             for (int k = 0; k < 4; k++){
//                 auto [dx,dy] = dxy[k];
//                 int cc = cost;
//                 if (grid[i][j] != k+1)
//                     cc++;
//                 dx += i; dy += j;
//                 if (dx >= 0 && dx < n && dy >= 0 && dy < m && cc < dp[dx][dy]){
//                     dp[dx][dy] = cc;
//                     pq.push({cc,dx,dy});
//                 }
//             }
//         }
//         return -1;
//     }
// };


const int dx[5] = {0, 1, -1, 0, 0};
const int dy[5] = {0, 0, 0, 1, -1};
typedef pair<int, int> pii;

class Solution {
public:
    int minCost(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        deque<pii> pq;
        pq.push_back(make_pair(0, 0));
        vector<vector<bool>> vis(n, vector<bool>(m));
        while (!pq.empty()) {
            pii f = pq.front();
            pq.pop_front();
            int y = f.second / m, x = f.second % m;
            if (vis[y][x]) continue;
            vis[y][x] = true;
            if (y == n - 1 && x == m - 1)
                return f.first;
            for (int k = 1; k <= 4; ++k) {
                int nx = x + dx[k], ny = y + dy[k];
                if (nx < 0 || nx >= m || ny < 0 || ny >= n)
                    continue;
                if (grid[y][x] == k) 
                    pq.push_front(make_pair(f.first, ny * m + nx));
                else
                    pq.push_back(make_pair(f.first + 1, ny * m + nx));
            }
        }
        return 0;
    }
};


// 作者：lucifer1004
// 链接：https://leetcode-cn.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/solution/zui-duan-lu-jing-suan-fa-bfs0-1bfsdijkstra-by-luci/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。