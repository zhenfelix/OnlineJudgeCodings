class Solution {
public:
    int minimumTimeRequired(vector<int>& jobs, int K) {
        int n = jobs.size();
        vector<int> dp, cost(1<<n, 0);
        unordered_map<int,int> mp;
        for (int j = 0; j < n; j++)
            mp[1<<j] = j;
        for (int s = 1; s < (1<<n); s++){
            cost[s] = cost[s&(s-1)] + jobs[mp[s&(-s)]];
        }
        dp = cost;
        for (int k = 1; k < K; k++){
            for (int s = (1<<n)-1; s > 0; s--){
                for (int i = s; i; i = (i-1)&s){
                    dp[s] = min(dp[s], max(cost[i],dp[s^i]));
                }
                if (k == K-1)
                    break;
            }
        }
        return dp.back();
    }
};
