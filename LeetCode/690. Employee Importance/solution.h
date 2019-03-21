/*
// Employee info
class Employee {
public:
    // It's the unique ID of each node.
    // unique id of this employee
    int id;
    // the importance value of this employee
    int importance;
    // the id of direct subordinates
    vector<int> subordinates;
};
*/
class Solution {
public:
    map<int,Employee*> id2e;
    int dfs(int id){
        int ans=id2e[id]->importance;
        for(auto s: id2e[id]->subordinates){
            ans+=dfs(id2e[s]->id);
        }
        return ans;
    }
    int getImportance(vector<Employee*> employees, int id) {
        for(auto e: employees){
            id2e[e->id]=e;
        }
        return dfs(id);
    }
};