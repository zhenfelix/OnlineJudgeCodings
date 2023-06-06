class Solution {
public:
    long long matrixSumQueries(int n, vector<vector<int>>& queries) {
        vector<unordered_set<int>> visited{unordered_set<int>(),unordered_set<int>()};
        long long ans = 0;
        int q = queries.size();
        for (int i = q - 1; i >= 0; i--) {
            int tpe = queries[i][0];
            int idx = queries[i][1];
            long long val = queries[i][2];
            if (visited[tpe].count(idx)) continue;
            visited[tpe].insert(idx);
            ans += val*(n-(int)visited[1-tpe].size());
        }
        return ans;
    }
};