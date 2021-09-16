const int maxn = 100;
bitset<maxn> f[maxn];

class Solution {
public:
    vector<bool> checkIfPrerequisite(int n, vector<vector<int>>& prerequisites, vector<vector<int>>& queries) {
        for (int i = 0; i < n; i++)
            f[i] = 0;
        for (auto p : prerequisites)
            f[p[1]][p[0]] = 1;
        for (int k = 0; k < n; k++){
            for (int i = 0; i < n; i++){
                if (f[i][k])
                    f[i] = f[i] | f[k];
            }
        }
        int m = queries.size();
        vector<bool> ans(m,false);
        for (int i = 0; i < m; i++)
            if (f[queries[i][1]][queries[i][0]])
                ans[i] = true;
        return ans;
    }
};