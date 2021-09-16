class Solution {
public:
    vector<int> maximizeXor(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size(), m = queries.size();
        vector<int> ans(m,-1);
        vector<pair<int,int>> pp;
        vector<vector<int>> trie(1,vector<int>(2,-1));
        int tail = 0;
        auto insert = [&](int x){
            int cur = 0;
            for (int i = 29; i >= 0; i--){
                int idx = (x>>i)&1;
                if (trie[cur][idx] == -1){
                    trie[cur][idx] = trie.size();
                    trie.push_back({-1,-1});
                }
                cur = trie[cur][idx];
            }
        };

        auto query = [&](int y){
            if (trie.size() == 1)
                return -1;
            int cur = 0, q = 0;
            for (int i = 29; i >= 0; i--){
                int idx = ((y>>i)&1)^1;
                if (trie[cur][idx] == -1)
                    idx = 1^idx;
                cur = trie[cur][idx];
                q = (q<<1)|(idx^((y>>i)&1));
            }
            return q;
        };

        sort(nums.begin(), nums.end());
        for (int i = 0; i < m; i++)
            pp.push_back({queries[i][1],i});
        sort(pp.begin(), pp.end());
        int i = 0;
        for (auto [mx, j] : pp){
            bool flag = true;
            for (;i < n && nums[i] <= mx; i++){
                insert(nums[i]);
                flag = false;
            }
            if (flag)
                break;
            ans[j] = query(queries[j][0]);
        }
        return ans;
    }
};