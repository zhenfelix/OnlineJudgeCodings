/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    void dfs(TreeNode* cur, set<int> &seen){
        if (!cur)
            return;
        seen.insert(cur->val);
        dfs(cur->left, seen);
        dfs(cur->right, seen);
    }
    int numColor(TreeNode* root) {
        set<int> seen;
        dfs(root, seen);
        return seen.size();
    }
};
