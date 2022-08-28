using pii = pair<int,int>;
using ll = long long;
class Solution {
public:
    long long minCostToTravelOnDays(vector<int>& days, vector<vector<int>>& tickets) {
        int n = days.size();
        vector<ll> dp(n+1, LLONG_MAX);
        dp[0] = 0;
        for (int i = 0; i < n; i++){
            int s = days[i];
            for (auto t: tickets){
                int j = upper_bound(days.begin(), days.end(), s+t[0]-1)-days.begin();
                j = min(j, n);
                dp[j] = min(dp[j], dp[i]+t[1]);
            }
        }
        return dp[n];
    }
};

