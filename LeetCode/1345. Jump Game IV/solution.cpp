class Solution {
public:
    int minJumps(vector<int>& arr) {
        int n = arr.size();
        vector<int> dp(n,n);
        unordered_map<int,vector<int>> mp;
        for (int i = 0; i < n; i++)
            mp[arr[i]].push_back(i);
        dp[0] = 0;
        queue<int> q;
        q.push(0);
        while (!q.empty()){
            int i = q.front(); q.pop();
            if (i == n-1)
                return dp[i];
            if (i-1 >= 0 && dp[i-1] > dp[i]+1){
                dp[i-1] = dp[i]+1;
                q.push(i-1);
            }
            if (i+1 < n && dp[i+1] > dp[i]+1){
                dp[i+1] = dp[i]+1;
                q.push(i+1);
            }
            for (auto j : mp[arr[i]]){
                if (j == i)
                    continue;
                if (dp[j] > dp[i]+1){
                    dp[j] = dp[i]+1;
                    q.push(j);
                }
            }
            mp[arr[i]].clear();
        }
        return -1;
    }
};