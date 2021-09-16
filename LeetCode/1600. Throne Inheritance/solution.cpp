class ThroneInheritance {
    string root;
    unordered_map<string,vector<string>> children;
    unordered_set<string> dead;

    void dfs(string cur, vector<string> &order){
        if (dead.find(cur) == dead.end())
            order.push_back(cur);
        for (string &nxt : children[cur]){
            dfs(nxt, order);
        }
    }
public:
    ThroneInheritance(string kingName) {
        root = kingName;
    }
    
    void birth(string parentName, string childName) {
        children[parentName].push_back(childName);
    }
    
    void death(string name) {
        dead.insert(name);
    }
    
    vector<string> getInheritanceOrder() {
        vector<string> order;
        dfs(root, order);
        return order;
    }
};

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * ThroneInheritance* obj = new ThroneInheritance(kingName);
 * obj->birth(parentName,childName);
 * obj->death(name);
 * vector<string> param_3 = obj->getInheritanceOrder();
 */