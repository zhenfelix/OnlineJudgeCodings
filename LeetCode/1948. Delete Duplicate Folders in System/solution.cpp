// // OJ: https://leetcode.com/contest/weekly-contest-251/problems/delete-duplicate-folders-in-system/
// // Author: github.com/lzl124631x
// // Time: O(NWlogC) where `N` is the number of folders, `W` is the max length of folder name, and `C` is the maximum number of direct subfolders.
// // Space: O(N^2 * W)
// struct Node {
//     string name;
//     map<string, Node*> next; // mapping from folder name to the corresponding child node.
//     bool del = false; // whether this folder is deleted.
//     Node(string n = "") : name(n) {}
// };
// class Solution {
//     void addPath(Node *node, vector<string> &path) { // Given a path, add nodes to the folder tree. This is similar to the Trie build process.
//         for (auto &s : path) {
//             if (node->next.count(s) == 0) node->next[s] = new Node(s);
//             node = node->next[s];
//         }
//     }
//     unordered_map<string, Node*> seen; // mapping from subfolder structure string to the first occurrence node.
//     string dedupe(Node *node) { // post-order traversal to dedupe. If we've seen the subfolder structure before, mark it as deleted.
//         string subfolder;
//         for (auto &[name, next] : node->next) {
//             subfolder += dedupe(next);
//         }
//         if (subfolder.size()) { // leaf nodes should be ignored
//             if (seen.count(subfolder)) { // if we've seen this subfolder structure before, mark them as deleted.
//                 seen[subfolder]->del = node->del = true;
//             } else {
//                 seen[subfolder] = node; // otherwise, add the mapping
//             }
//         }
//         return "(" + node->name + subfolder + ")"; // return the folder structure string of this node.
//     }
//     vector<vector<string>> ans;
//     vector<string> path;
//     void getPath(Node *node) {
//         if (node->del) return; // if the current node is deleted, skip it.
//         path.push_back(node->name);
//         ans.push_back(path);
//         for (auto &[name, next] : node->next) {
//             getPath(next);
//         }
//         path.pop_back();
//     }
// public:
//     vector<vector<string>> deleteDuplicateFolder(vector<vector<string>>& A) {
//         Node root;
//         for (auto &path : A) addPath(&root, path);
//         dedupe(&root);
//         for (auto &[name, next] : root.next) getPath(next);
//         return ans;
//     }
// };

using ull = unsigned long long;
const int P = 129;

struct Node {
    string name;
    map<string, Node*> children;
    ull hash = 0;
    bool deleted = false;

    Node(string name): name(name) {}
};

unordered_map<ull, vector<Node*>> mp;
vector<vector<string>> ans;

void dfs(Node *p) {
    string sub;
    for (auto [name, node] : p->children) {
        dfs(node);
        sub += name + to_string(node->hash) + "/";
    }
    for (char ch : sub)
        p->hash = p->hash * P + ch;
    if (!p->children.empty())
        mp[p->hash].emplace_back(p);
}

void dfs2(Node *p, vector<string> &curr) {
    if (!p->deleted) {
        if (p->name != "/") {
            curr.push_back(p->name);
            ans.push_back(curr);
        }
        for (auto [_name, node] : p->children)
            dfs2(node, curr);
        if (p->name != "/")
            curr.pop_back();
    }
}

class Solution {
public:
    vector<vector<string>> deleteDuplicateFolder(vector<vector<string>>& paths) {
        Node *root = new Node("/");
        for (auto &path : paths) {
            Node *p = root;
            for (string &dir : path) {
                if (!p->children.count(dir))
                    p->children[dir] = new Node(dir);
                p = p->children[dir];
            }
        }
        
        mp.clear();
        dfs(root);
        for (auto [hash, nodes] : mp) {
            
            if (nodes.size() >= 2) {
                for (Node *node : nodes){
                    // cout << node->name << endl;
                    node->deleted = true;
                }
                    
            }
        }
        
        ans.clear();
        vector<string> curr;
        dfs2(root, curr);
        return ans;
    }
};