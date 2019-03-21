// class Solution {
// public:

//     vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
//         int n=graph.size();
//         vector<vector<int>> reverse_graph(n, vector<int>(0));
//         vector<int> income, ans;
//         vector<bool> mark(n, false);
//         queue<int> q;
//         for(auto x: graph){
//             for(auto xx: x){
//                 reverse_graph[xx].push_back(income.size());
//             }
//             income.push_back(x.size());
//             if(income.back()==0)q.push(income.size()-1);
//         }
//         while(!q.empty()){
//             int tmp=q.front();
//             q.pop();mark[tmp]=true;
//             for(auto x: reverse_graph[tmp]){
//                 income[x]--;
//                 if(income[x]==0)q.push(x);
//             }
//         }
//         for(int i=0;i<n;i++)if(mark[i])ans.push_back(i);
//         return ans;
//     }
// };


// Let us perform a "brute force": a cycle-finding DFS algorithm on each node individually. This is a classic "white-gray-black" DFS algorithm that would be part of any textbook on DFS. We mark a node gray on entry, and black on exit. If we see a gray node during our DFS, it must be part of a cycle. In a naive view, we'll clear the colors between each search.

class Solution {
public:
    bool dfs(vector<vector<int>>& graph, vector<int> &color, int cur){
        if(color[cur]==2)return true;
        if(color[cur]==1)return false;
        color[cur]=1;
        for(auto x: graph[cur]){
            if(!dfs(graph, color, x))return false;
        }
        color[cur]=2;
        return true;
    }

    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n=graph.size();
        vector<int> color(n, 0), ans;
        for(int i=0;i<n;i++){
            if(dfs(graph, color, i))ans.push_back(i);
        }
        return ans;
    }
};