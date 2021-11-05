using tiii = tuple<int,int,int>;

class Solution {
public:
    int kthSmallest(vector<vector<int>>& mat, int k) {
        vector<int> cur = {0};
        int n = mat.size(), m = mat[0].size();
        for (int i = 0; i < n; i++){
            priority_queue<tiii, vector<tiii>> pq;
            vector<int> nxt;
            for (int j = 0; j < m; j++){
                pq.push({-(cur[0]+mat[i][j]),j,0});
            }
            for (int j = 0; j < k && !pq.empty(); j++){
                auto [s,p,q] = pq.top(); pq.pop();
                nxt.push_back(-s);
                if (q+1 < cur.size())
                    pq.push({-(mat[i][p]+cur[q+1]),p,q+1});
            }
            swap(cur,nxt);
        }
        return cur.back();
    }
};