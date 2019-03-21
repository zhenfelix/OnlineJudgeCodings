class Solution {
public:
    bool dfs(vector<vector<int>>& graph, vector<int> &mark, int id, int flag){
        if(mark[id]!=0)return mark[id]==flag;
        mark[id]=flag;
        flag*=-1;
        for(auto x: graph[id]){
            if(dfs(graph,mark,x,flag)==false)return false;
        }
        return true;
    }
    bool isBipartite(vector<vector<int>>& graph) {
        int n=graph.size();
        vector<int> mark(n,0);
        for(int i=0;i<n;i++){
            if(mark[i]==0 && dfs(graph,mark,i,-1)==false)return false;
        }
        return true;
    }
};