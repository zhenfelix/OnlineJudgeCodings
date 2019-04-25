// luogu-judger-enable-o2
#include <cstdio>
#include<iostream>
#include<vector>
#include <algorithm>
using namespace std;


class Solution {
public:
    double solve(vector<double>& nums, int k) {
        int n=nums.size();
        vector<double> dp(k+1,0);
        //        sort(nums.begin(), nums.end(), [] (double a, double b){return a>=b;} );
        sort(nums.begin(), nums.end(), greater<double>());
        for(int i=1;i<=k;i++)dp[i]=nums[0]/(double)i;
        for(int i=1;i<n && i<=k;i++){
            vector<double> tmp(dp);
            bool flag=true;
            for (int j=k; j>=1; j--) {
//                tmp[j]=dp[j];
                bool noUpdate=true;
                for(int m=1;j-m>0;m++){
                    double choice=min(dp[j-m],nums[i]/(double)(m));
                    if(choice<tmp[j])break;
                    tmp[j]=choice;
                    noUpdate=false;
                }
                if(noUpdate)break;
                flag=false;
            }
            if(flag)break;
            dp=tmp;
        }
        return dp[k];
    }
};


int main(int argc, char const *argv[])
{
     freopen("input.txt", "r", stdin);
    int n,k;
    cin>>n>>k;
    vector<double>nums(n);
    for(int i=0;i<n;i++) {
        cin>>nums[i];
    }
    Solution s;
//    printf("%.2f\n",s.solve(nums, k));
    cout<<s.solve(nums, k)<<endl;
    return 0;
}

