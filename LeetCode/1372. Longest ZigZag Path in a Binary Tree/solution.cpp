/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
using tiii = tuple<int,int,int>;
class Solution {
public:
    tiii dfs(TreeNode *root){
        if (!root)
            return {0,0,0};
        auto [ll,lr,ld] = dfs(root->left);
        auto [rl,rr,rd] = dfs(root->right);
        int d = max(ld,rd);
        d = max(d,lr+1);
        d = max(d,rl+1);
        return {lr+1,rl+1,d};
    }
    int longestZigZag(TreeNode* root) {
        auto [l,r,d] = dfs(root);
        return d-1;
    }
};