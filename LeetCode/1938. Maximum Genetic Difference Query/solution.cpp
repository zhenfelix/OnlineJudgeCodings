// const int N = 20;
// const int maxn = 1<<N;
// int tree[maxn];

// class Solution {
// public:
//     vector<int> maxGeneticDifference(vector<int>& parents, vector<vector<int>>& queries) {
//         memset(tree, 0, maxn*sizeof(int));
//         int n = parents.size();
//         vector<vector<int>> g(n, vector<int>());
//         int root = -1;
//         for (int i = 0; i < n; i++){
//             if (parents[i] == -1)
//                 root = i;
//             else
//                 g[parents[i]].push_back(i);
//         }
//         int m = queries.size();
//         unordered_map<int,vector<int>> mp;
//         for (int i = 0; i < m; i++){
//             mp[queries[i][0]].push_back(i);
//         }
//         vector<int> ans(m, 0);
//         dfs(root, g, mp, queries, ans);
//         return ans;
//     }

//     void dfs(int root, vector<vector<int>> &g, unordered_map<int, vector<int>> &mp, vector<vector<int>>& queries, vector<int> &ans){
//         add(root);
//         for (auto i : mp[root]){
//             int val = queries[i][1], res = 0, cur = 0;
//             for (int bit = N-2; bit >= 0; bit--){
//                 int delta = (val>>bit)&1;
//                 if (tree[cur*2+2-delta]){
//                     res |= (1<<bit);
//                     cur = cur*2+2-delta;
//                 }
//                 else{
//                     cur = cur*2+1+delta;
//                 }
//             }
//             ans[i] = res;
//         }
//         for (auto child : g[root])
//             dfs(child, g, mp, queries, ans);
//         remove(root);
//         return;
//     }
//     void add(int val){
//         int cur = 0;
//         tree[cur]++;
//         for (int bit = N-2; bit >= 0; bit--){
//                 int delta = (val>>bit)&1;
//                 cur = cur*2+1+delta;
//                 tree[cur]++;
//             }
//     }
//     void remove(int val){
//         int cur = 0;
//         tree[cur]--;
//         for (int bit = N-2; bit >= 0; bit--){
//                 int delta = (val>>bit)&1;
//                 cur = cur*2+1+delta;
//                 tree[cur]--;
//             }
//     }
// };


const int N = 20;
const int maxn = 1<<N;
int tree[maxn];

class Solution {
public:
    vector<int> maxGeneticDifference(vector<int>& parents, vector<vector<int>>& queries) {
        memset(tree, 0, maxn*sizeof(int));
        int n = parents.size();
        vector<vector<int>> g(n, vector<int>());
        int root = -1;
        for (int i = 0; i < n; i++){
            if (parents[i] == -1)
                root = i;
            else
                g[parents[i]].push_back(i);
        }
        int m = queries.size();
        unordered_map<int,vector<int>> mp;
        for (int i = 0; i < m; i++){
            mp[queries[i][0]].push_back(i);
        }
        vector<int> ans(m, 0);
        dfs(root, g, mp, queries, ans);
        return ans;
    }

    void dfs(int root, vector<vector<int>> &g, unordered_map<int, vector<int>> &mp, vector<vector<int>>& queries, vector<int> &ans){
        update(root, 1);
        for (auto i : mp[root]){            
            ans[i] = getMax(queries[i][1]);
        }
        for (auto child : g[root])
            dfs(child, g, mp, queries, ans);
        update(root, -1);
        return;
    }
    void update(int val, int inc){
        int cur = 0;
        tree[cur] += inc;
        for (int bit = N-2; bit >= 0; bit--){
                int delta = (val>>bit)&1;
                cur = cur*2+1+delta;
                tree[cur] += inc;
            }
    }
    int getMax(int val){
        int cur = 0, res = 0;
        for (int bit = N-2; bit >= 0; bit--){
                int delta = (val>>bit)&1;
                if (tree[cur*2+2-delta]){
                    res |= (1<<bit);
                    cur = cur*2+2-delta;
                }
                else{
                    cur = cur*2+1+delta;
                }
            }
        return res;
    }
};