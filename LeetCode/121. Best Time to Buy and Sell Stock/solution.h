#include <vector>
#include <string>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;

// class Solution {
// public:
//     int maxProfit(vector<int>& prices) {
//         vector<int> sell;
//         int mx=0,ans=0;
//         for(int i=prices.size()-1;i>=0;i--){
//             if(prices[i]>mx)mx=prices[i];
//             sell.push_back(mx);
//         }
//         for(int i=0;i<prices.size();i++){
//             int tmp=sell[prices.size()-1-i]-prices[i];
//             if(tmp>ans)ans=tmp;
//         }
//         return ans;
//     }
// };

// class Solution {
// public:
//     int maxProfit(vector<int>& prices) {
//         vector<int> buy;
//         int mi=1<<31-1,ans=0;
//         for(auto x: prices){
//             if(mi>x)mi=x;
//             buy.push_back(mi);
//         }
//         for(int i=0;i<prices.size();i++){
//             if(prices[i]-buy[i]>ans)ans=prices[i]-buy[i];
//         }
//         return ans;
//     }
// };
    
class Solution {
    
public:
    int maxProfit(vector<int>& prices)
    {
        int maxprofit=0;
        int minvalue=INT_MAX;
        for(int i=0;i<prices.size();i++)
        {
            if(minvalue>prices[i])
                minvalue=prices[i];
            if(prices[i]-minvalue>maxprofit)
                maxprofit=prices[i]-minvalue;
                
        }
        return maxprofit;
    }
};