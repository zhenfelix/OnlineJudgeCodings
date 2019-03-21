//Three C++ solutions BFS, DFS, and BF
//https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/128217/Three-C++-solutions-BFS-DFS-and-BF

// class Solution {
// public:
//         int findCheapestPrice(int n, vector<vector<int>>& flights, int s, int d, int K) {
//        unordered_map<int, vector<pair<int,int>>> g;
//        for (const auto& e : flights)
//             g[e[0]].emplace_back(e[1], e[2]);        
//         int ans = INT_MAX;
//         vector<int> visited(n,0);
//         dfs(s, d, K + 1, 0, visited, ans, g);
//         return ans == INT_MAX ? - 1 : ans;
//     }
    
//     void dfs(int s, int d, int k, int cost, vector<int>& visited, int& ans, unordered_map<int, vector<pair<int,int>>>& g ) {
//         if (s == d) { ans = cost; return; }
//         if (k == 0) return; 
//         visited[s]=1;
//         for (const auto& x : g[s]) {
//           if (visited[x.first]==0){
//               if (cost + x.second > ans) continue; // IMPORTANT!!! prunning 
     
//               dfs(x.first, d, k - 1, cost + x.second, visited, ans, g); 
             
//           }
//         }
//          visited[s] = 0;
//   }
// };

// class Solution {
// public:
//             int findCheapestPrice(int n, vector<vector<int>>& flights, int s, int d, int K) {
//        unordered_map<int, vector<pair<int,int>>> g;
//         vector<bool> visited(n, false);
//        for (const auto& e : flights)
//             g[e[0]].emplace_back(e[1], e[2]);        
//         int ans = INT_MAX;
//         queue<pair<int,int>> q;q.push({s,0}); 
        
//         int steps =0; 
//         while(!q.empty()){
//             int n = q.size();
//             for(int i=0; i<n; ++i){
//              auto curr=q.front();q.pop();
//             if(curr.first == d) ans = min(ans, curr.second);   
//             for(auto x:  g[curr.first]){             
//                if( curr.second + x.second > ans) continue;
//                 q.push({x.first,curr.second + x.second });
//              }  
//             }
//           if(steps++ > K) break;
//         }
        
//         return ans == INT_MAX ? - 1 : ans;
//     } 
// };


class Solution {
public:
          int findCheapestPrice(int n, vector<vector<int>>& flights, int s, int d, int K) {
        const int INF = 1e9;
        vector<vector<int>> dp(K + 2, vector<int>(n, INF));
        dp[0][s] = 0;        
         for (int i = 1; i <= K + 1; ++i) {
            dp[i][s] = 0;
            for (const auto& x : flights)
                  dp[i][x[1]] = min(dp[i][x[1]], dp[i-1][x[0]] + x[2]);    
            }
            return dp[K + 1][d] >= INF ? -1 : dp[K + 1][d];
            
        } 
};