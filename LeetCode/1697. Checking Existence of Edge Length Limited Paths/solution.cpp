class Solution {
public:
    vector<bool> distanceLimitedPathsExist(int n, vector<vector<int>>& edgeList, vector<vector<int>>& queries) {
        sort(edgeList.begin(), edgeList.end(), [&](vector<int> &a, vector<int> &b){
            return a.back() < b.back();
        });
        int m = queries.size();
        vector<int> idx, parent(n);
        vector<bool> ans(m);
        for (int i = 0; i < m; i++)
            idx.push_back(i);
        sort(idx.begin(), idx.end(), [&](int a, int b){
            return queries[a].back() < queries[b].back();
        });
        for (int i = 0; i < n; i++)
            parent[i] = i;

        function<int(int)> find = [&](int root) -> int {
            if (parent[root] != root)
                parent[root] = find(parent[root]);
            return parent[root];
        };

        function<void(int,int)> merge = [&](int a, int b) -> void {
            int ra = find(a), rb = find(b);
            parent[ra] = rb;
            return;
        };
        int j = 0;
        for (auto i : idx){
            for (; j < edgeList.size() && edgeList[j].back() < queries[i].back(); j++){
                merge(edgeList[j][0], edgeList[j][1]);
            }
            if (find(queries[i][0]) == find(queries[i][1]))
                ans[i] = true;
            else
                ans[i] = false;
        }
        return ans;
    }
};



class Solution {
public:
    vector<bool> distanceLimitedPathsExist(int n, vector<vector<int>>& edgeList, vector<vector<int>>& queries) {
        sort(edgeList.begin(), edgeList.end(), [&](vector<int> &a, vector<int> &b){
            return a.back() < b.back();
        });
        int m = queries.size();
        vector<int> idx, parent(n), sz(n,1);
        vector<bool> ans(m);
        for (int i = 0; i < m; i++)
            idx.push_back(i);
        sort(idx.begin(), idx.end(), [&](int a, int b){
            return queries[a].back() < queries[b].back();
        });
        for (int i = 0; i < n; i++)
            parent[i] = i;

        function<int(int)> find = [&](int root) -> int {
            if (parent[root] != root)
                parent[root] = find(parent[root]);
            return parent[root];
        };

        function<void(int,int)> merge = [&](int a, int b) -> void {
            int ra = find(a), rb = find(b);
            if (ra == rb)
                return;
            if (sz[ra] < sz[rb]){
                parent[ra] = rb;
                sz[rb] += sz[ra];
            }
            else{
                parent[rb] = ra;
                sz[ra] += sz[rb];
            }
            return;
        };
        int j = 0;
        for (auto i : idx){
            for (; j < edgeList.size() && edgeList[j].back() < queries[i].back(); j++){
                merge(edgeList[j][0], edgeList[j][1]);
            }
            if (find(queries[i][0]) == find(queries[i][1]))
                ans[i] = true;
            else
                ans[i] = false;
        }
        return ans;
    }
};
