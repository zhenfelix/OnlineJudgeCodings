const int inf = 0x3f3f3f3f;

class Solution {
public:
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        vector<vector<int>> dis(n, vector<int>(n,inf));
        for (int i = 0; i < n; i++)
            dis[i][i] = 0;
        for (auto e : edges){
            dis[e[0]][e[1]] = e[2];
            dis[e[1]][e[0]] = e[2];
        }
        for (int i = 0; i < n; i++){
            for (int u = 0; u < n; u++){
                for (int v = 0; v < n; v++){
                    dis[u][v] = min(dis[u][v], dis[u][i]+dis[i][v]);
                }
            }
        }
        int idx = -1, cnt = inf;
        for (int u = 0; u < n; u++){
            int cc = 0;
            for (int v = 0; v < n; v++)
                if (dis[u][v] <= distanceThreshold)
                    cc++;
            if (cc <= cnt){
                cnt = cc;
                idx = u;
            }
        }
        return idx;
    }
};