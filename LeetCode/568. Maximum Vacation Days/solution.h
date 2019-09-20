class Solution {
public:
    int maxVacationDays(vector<vector<int>>& flights, vector<vector<int>>& days) {
        int n = flights.size();
        int k = days[0].size();
        for(int i=0;i<n;i++){
            flights[i][i] = 1;
        }
        vector<int> dp(n,INT_MIN);
        dp[0] = 0;
        for(int d=0;d<k;d++){
            vector<int> tmp(dp.begin(), dp.end());
            for(int end=0;end<n;end++){
                for(int start=0;start<n;start++){
                    if(flights[start][end] == 1){
                        tmp[end] = max(tmp[end], dp[start]+days[end][d]);
                    }
                }
            }
            dp = tmp;
                
        }
        return *max_element(dp.begin(), dp.end());
    }
};