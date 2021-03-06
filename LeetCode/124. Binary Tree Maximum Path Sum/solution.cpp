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
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int res = -1e8;
        dfs(root,res);
        return res;
    }
    int dfs(TreeNode* root, int &res){
        if(!root)return 0;
        int left = dfs(root->left, res);
        int right = dfs(root->right, res);
        res = max(res, root->val+max(0,left)+max(0,right));
        return max(0,max(left,right))+root->val;
    }
};


class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int res = INT_MIN;
        dfs(root,res);
        return res;
    }
    int dfs(TreeNode* root, int &res){
        if(!root)return 0;
        int left = max(dfs(root->left, res),0);
        int right = max(dfs(root->right, res),0);
        res = max(res, root->val+left+right);
        return max(left,right)+root->val;
    }
};