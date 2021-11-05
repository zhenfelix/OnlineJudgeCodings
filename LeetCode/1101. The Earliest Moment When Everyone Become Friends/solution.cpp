class Solution {
public:
    int earliestAcq(vector<vector<int>>& logs, int n) {
        vector<int> f(n);
        for (int i = 0; i < n; i++)
            f[i] = i;
        function<int(int)> find = [&](int x){
            if (f[x] != x)
                f[x] = find(f[x]);
            return f[x];
        };
        auto merge = [&](int u, int v){
            int ru = find(u), rv = find(v);
            if (ru != rv){
                f[ru] = rv;
                return true;
            }
            return false;
        };
        sort(logs.begin(), logs.end());
        int cnt = 0;
        for (auto log : logs){
            int u = log[1], v = log[2];
            if (merge(u,v))
                cnt++;
            if (cnt == n-1)
                return log[0];
        }
        return -1;
    }
};