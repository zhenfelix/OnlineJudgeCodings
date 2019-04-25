#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <algorithm>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <iostream>
#include <deque>

using namespace std;

class Solution {
public:
    double solve(vector<double>& nums, int k) {
        int n=nums.size();
        vector<double> dp(k+1,0);
        sort(nums.begin(), nums.end(), [] (double a, double b){return a>=b;} );
        for(int i=1;i<=k;i++)dp[i]=nums[0]/(double)i;
        for(int i=1;i<n;i++){
            vector<double> tmp(k+1,0);
            for (int j=1; j<=k; j++) {
                tmp[j]=dp[j];
                for(int m=1;j-m>0;m++){
                    double choice=min(dp[j-m],nums[i]/(double)(m));
                    if(choice<tmp[j])break;
                    tmp[j]=choice;
                }
            }
            dp=tmp;
        }
        
        return dp[k];
    }
};
