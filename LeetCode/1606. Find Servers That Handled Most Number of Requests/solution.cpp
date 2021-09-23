class Solution {
public:
    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
        set<int> available;  
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> busy;
        int n = arrival.size();
        for (int i = 0; i < k; i++)
            available.insert(i);
        vector<int> cnt(k,0);
        for (int i = 0; i < n; i++){
            int t = arrival[i];
            while (!busy.empty() && busy.top().first <= t){
                auto [_,idx] = busy.top();busy.pop();
                available.insert(idx);
            }
            if (available.lower_bound(i%k) != available.end()){
                int j = *available.lower_bound(i%k);
                available.erase(j);
                busy.push({load[i]+t,j});
                cnt[j]++;
            }
            else if (!available.empty()){
                int j = *available.begin();
                available.erase(j);
                busy.push({load[i]+t,j});
                cnt[j]++;
            }
        }
        int mx = *max_element(cnt.begin(), cnt.end());
        vector<int> res;
        for (int i = 0; i < k; i++)
            if (cnt[i] == mx)
                res.push_back(i);
        return res;
    }
};