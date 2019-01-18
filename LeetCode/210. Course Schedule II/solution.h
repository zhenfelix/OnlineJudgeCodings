// class Solution {
// public:
//     vector<int> findOrder(int numCourses, vector<pair<int, int>>& prerequisites) {
//         vector<vector<int>> graph(numCourses,vector<int>(0));
//         vector<int> pre(numCourses,0);
//         vector<int> ans;
//         queue<int> q;
//         for(auto p: prerequisites){
//             pre[p.first]++;
//             graph[p.second].push_back(p.first);
//         }
//         for(int i=0;i<numCourses;i++)if(pre[i]==0)q.push(i);
//         while(!q.empty()){
//             int tmp=q.front();q.pop();ans.push_back(tmp);
//             for(auto v: graph[tmp]){
//                 pre[v]--;
//                 if(pre[v]==0)q.push(v);
//             }
//         }
//         if(ans.size()!=numCourses)ans.clear();
//         return ans;
        
//     }
// };
// indegree method topological sort

class Solution {
public:
    void dfs(int node, vector<vector<int>> &graph, stack<int> &st, vector<int> &state, bool &isCycle){
        if(isCycle)return;
        state[node]=-1;
        for(auto x: graph[node]){
            if(state[x]==-1){isCycle=true;break;}
            if(state[x]==0)dfs(x,graph,st,state,isCycle);
        }
        state[node]=1;
        st.push(node);
        return;
    }
    vector<int> findOrder(int numCourses, vector<pair<int, int>>& prerequisites) {
        bool isCycle=false;
        vector<vector<int>> graph(numCourses,vector<int>(0));
        stack<int> st;vector<int> ans;vector<int> state(numCourses,0);
        for(auto p: prerequisites)graph[p.second].push_back(p.first);
        for(int i=0;i<numCourses;i++){
            if(state[i]==0)dfs(i,graph,st,state,isCycle);
        }
        if(isCycle)return ans;
        else{
            while(!st.empty()){
                ans.push_back(st.top());st.pop();
            }
            return ans;
        }
    }
};
//dfs method