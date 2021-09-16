class Solution {
public:
    int checkWays(vector<vector<int>>& pairs) {
        unordered_map<int,int> cnt, mp;
        unordered_map<int,vector<int>> graph;
        int ans = 1;
        for (auto p : pairs){
            cnt[p[0]]++;
            cnt[p[1]]++;
            graph[p[0]].push_back(p[1]);
            graph[p[1]].push_back(p[0]);
        }
        int n = cnt.size();
        vector<int> idx, parent(n, -1);
        for (auto [k,v] : cnt){
            idx.push_back(k);
        }
        sort(idx.begin(), idx.end(), [&](int a, int b){
            if (cnt[a] == cnt[b])
                return a < b;
            return cnt[a] > cnt[b];
        });
        for (int i = 0; i < n; i++){
            mp[idx[i]] = i;
        }
        for (int i = 0; i < n; i++){
            int cur = idx[i];
            for (auto nxt : graph[cur]){
                if (mp[nxt] < i)
                    continue;
                if (i && parent[mp[nxt]] == -1)
                    return 0;
                if (cnt[cur] == cnt[nxt])
                    ans = 2;
                if (parent[i] != parent[mp[nxt]])
                    return 0;
                parent[mp[nxt]] = i;
            }
        }
        return ans;
    }
};