class Solution {
public:
    int reachableNodes(int n, vector<vector<int>>& edges, vector<int>& r) {
        set<int>s(r.begin(),r.end());
        vector<vector<int>>to(n);
        for(auto i:edges)to[i[0]].push_back(i[1]),to[i[1]].push_back(i[0]);
        int ret=0;
        function<void(int,int)>dfs=[&](int p,int f){
            if(s.count(p))return;
            ++ret;
            for(int i:to[p])if(i!=f)dfs(i,p);
        };
        dfs(0,-1);
        return ret;
    }
};