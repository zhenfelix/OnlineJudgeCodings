// class Solution {
// public:
//     vector<int> shortestDistanceColor(vector<int>& colors, vector<vector<int>>& queries) {
//         vector<vector<int>> idx(4);
//         int n = colors.size();
//         for (int i = 0; i < n; i++)
//             idx[colors[i]].push_back(i);
//         int m = queries.size();
//         vector<int> ans(m);
//         for (int i = 0; i < m; i++){
//             int j = queries[i][0];
//             int c = queries[i][1];
//             if (idx[c].empty()){
//                 ans[i] = -1;
//                 continue;
//             }
//             ans[i] = n;
//             auto it = lower_bound(idx[c].begin(), idx[c].end(), j);
//             if (it != idx[c].end())
//                 ans[i] = min(ans[i], *it-j);
            
//             if (it != idx[c].begin()){
//                 it--;
//                 ans[i] = min(ans[i], j-*it);
//             }
//         }
//         return ans;
//     }
// };

class Solution {
public:
    vector<int> shortestDistanceColor(vector<int>& colors, vector<vector<int>>& queries) {
        int n = colors.size();
        vector<vector<int>> dis(3, vector<int>(n, 1e9));
        for(int i = 0, a = -1, b = -1, c = -1; i < n; ++i){
            if(colors[i] == 1) a = i;
            else if(colors[i] == 2) b = i;
            else c = i;
            if(a != -1) dis[0][i] = min(dis[0][i], i - a);
            if(b != -1) dis[1][i] = min(dis[1][i], i - b);
            if(c != -1) dis[2][i] = min(dis[2][i], i - c);
        }
        for(int i = n - 1, a = -1, b = -1, c = -1; i >= 0; --i){
            if(colors[i] == 1) a = i;
            else if(colors[i] == 2) b = i;
            else c = i;
            if(a != -1) dis[0][i] = min(dis[0][i], a - i);
            if(b != -1) dis[1][i] = min(dis[1][i], b - i);
            if(c != -1) dis[2][i] = min(dis[2][i], c - i);
        }
        vector<int> ans(queries.size());
        for(int i = 0; i < queries.size(); ++i){
            int t = dis[queries[i][1] - 1][queries[i][0]];
            ans[i] = t == 1e9 ? -1 : t;
        }
        return ans;
    }
};


// 作者：Monologue-S
// 链接：https://leetcode-cn.com/problems/shortest-distance-to-target-color/solution/conyu-chu-li-o1qu-de-da-an-by-monologue-hk6rr/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。