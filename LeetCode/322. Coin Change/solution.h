// class Solution {
// public:
//     int coinChange(vector<int>& coins, int amount) {
//         int level=0,n=coins.size();
//         queue<int> nodes;
//         vector<bool> visit(amount+1,false);
//         nodes.push(amount);nodes.push(INT_MAX);visit[amount]=true;
//         // sort(coins.begin(),coins.end(),greater<int>());
//         while(1){
//             int node=nodes.front();nodes.pop();
//             if(node==0)return level;
//             if(nodes.empty())break;
//             if(node==INT_MAX){level++;nodes.push(INT_MAX);continue;}
//             for(auto x: coins){
//                 // if(x==node)return level+1;
//                 if(x<=node&&visit[node-x]==false){nodes.push(node-x);visit[node-x]=true;}
//             }
//         }
//         return -1;
//     }
// };
// bsf


const int inf = 0x3f3f3f3f;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount+1,inf);
        dp[0] = 0;
        int n = coins.size();
        for (int i = 0; i < n; i++){
            for (int w = coins[i]; w <= amount; w++)
                dp[w] = min(dp[w], dp[w-coins[i]]+1);
        }
        int res = dp.back();
        return res < inf ? res : -1;
    }
};




class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int Max = amount + 1;
        vector<int> dp(amount + 1, Max);
        dp[0] = 0;
        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < coins.size(); j++) {
                if (coins[j] <= i) {
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1);
                }
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
};
//dp