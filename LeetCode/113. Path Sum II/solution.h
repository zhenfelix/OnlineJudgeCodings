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
    void dfs(TreeNode *root, int sum, vector<int> &tmp, vector<vector<int>> &ans){
        if(!root)return;
        tmp.push_back(root->val);
        if(!root->left && !root->right && root->val==sum){
            ans.push_back(tmp);
        }
        else{
            dfs(root->left, sum-root->val, tmp, ans);
            dfs(root->right, sum-root->val, tmp, ans);
        }
        tmp.pop_back();
        return;
    }
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> ans;
        vector<int> tmp;
        dfs(root, sum, tmp ,ans);
        return ans;
    }
};