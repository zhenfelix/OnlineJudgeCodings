const int maxn = 65;

class Solution {
public:
    bool isPrintable(vector<vector<int>>& targetGrid) {
        int n = targetGrid.size(), m = targetGrid[0].size();
        vector<bool> colors(maxn,false);
        vector<int> lo(maxn,n), hi(maxn,-1), left(maxn,m), right(maxn,-1), degree(maxn,0);
        vector<vector<int>> graph(maxn);
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                int c = targetGrid[i][j];
                colors[c] = true;
                lo[c] = min(lo[c],i);
                hi[c] = max(hi[c],i);
                left[c] = min(left[c],j);
                right[c] = max(right[c],j);
            }
        }
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                int c = targetGrid[i][j];
                for (int nc = 1; nc < maxn; nc++){
                    if (nc == c || !colors[nc])
                        continue;
                    if (i >= lo[nc] && i <= hi[nc] && j >= left[nc] && j <= right[nc]){
                        degree[c]++;
                        graph[nc].push_back(c);
                    }
                }
            }
        }
        queue<int> q;
        for (int c = 1; c < maxn; c++)
            if (colors[c] && degree[c] == 0)
                q.push(c);
        while (!q.empty()){
            int cur = q.front();q.pop();
            for (auto nxt : graph[cur]){
                degree[nxt]--;
                if (degree[nxt] == 0)
                    q.push(nxt);
            }
        }
        for (int c = 1; c < maxn; c++)
            if (colors[c] && degree[c] != 0)
                return false;
        return true;
    }
};





const int inf = 0x3f3f3f3f;
const int maxn = 65;
bool colors[maxn];
int lo[maxn],hi[maxn],lft[maxn],rgt[maxn],degree[maxn];

class Solution {
public:
    bool isPrintable(vector<vector<int>>& targetGrid) {
        int n = targetGrid.size(), m = targetGrid[0].size();
        memset(colors,0,maxn*sizeof(bool));
        memset(lo,inf,maxn*sizeof(int));
        memset(lft,inf,maxn*sizeof(int));
        memset(hi,0,maxn*sizeof(int));
        memset(rgt,0,maxn*sizeof(int));
        memset(degree,0,maxn*sizeof(int));
        
        vector<vector<int>> graph(maxn);
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                int c = targetGrid[i][j];
                colors[c] = true;
                lo[c] = min(lo[c],i);
                hi[c] = max(hi[c],i);
                lft[c] = min(lft[c],j);
                rgt[c] = max(rgt[c],j);
            }
        }
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                int c = targetGrid[i][j];
                for (int nc = 1; nc < maxn; nc++){
                    if (nc == c || !colors[nc])
                        continue;
                    if (i >= lo[nc] && i <= hi[nc] && j >= lft[nc] && j <= rgt[nc]){
                        degree[c]++;
                        graph[nc].push_back(c);
                    }
                }
            }
        }
        queue<int> q;
        for (int c = 1; c < maxn; c++)
            if (colors[c] && degree[c] == 0)
                q.push(c);
        while (!q.empty()){
            int cur = q.front();q.pop();
            for (auto nxt : graph[cur]){
                degree[nxt]--;
                if (degree[nxt] == 0)
                    q.push(nxt);
            }
        }
        for (int c = 1; c < maxn; c++)
            if (colors[c] && degree[c] != 0)
                return false;
        return true;
    }
};