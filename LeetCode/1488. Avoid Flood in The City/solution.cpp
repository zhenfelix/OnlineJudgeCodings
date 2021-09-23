class Solution {
public:
    vector<int> avoidFlood(vector<int>& rains) {
        unordered_map<int,int> mp;  
        int n = rains.size();
        vector<int> ans(n,-1);
        set<int> idx;
        for (int i = 0; i < n; i++){
            if (rains[i] == 0){
                idx.insert(i);
                continue;
            }
            if (mp.count(rains[i])){
                if (idx.empty())
                    return {};
                auto it = idx.upper_bound(mp[rains[i]]);
                if (it == idx.end())
                    return {};
                ans[*it] = rains[i];
                idx.erase(it);
            }
            mp[rains[i]] = i;
        }
        for (auto i : idx)
            ans[i] = 1;
        return ans;
    }
};