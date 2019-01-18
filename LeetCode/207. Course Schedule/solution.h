class Solution {
public:
    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<int> pre(numCourses,0);
        vector<vector<int>> graph(numCourses,vector<int>(0));
        queue<int> q;
        for(auto p: prerequisites){
            int a=p.first,b=p.second;
            pre[a]++;
            graph[b].push_back(a);
        }
        for(int i=0;i<pre.size();i++)if(pre[i]==0)q.push(i);
        int cc=0;
        while(!q.empty()){
            int u=q.front();q.pop();cc++;
            for(auto v: graph[u]){
                pre[v]--;
                if(pre[v]==0)q.push(v);
            }
        }
        if(cc==numCourses)return true;
        else return false;
    }
};