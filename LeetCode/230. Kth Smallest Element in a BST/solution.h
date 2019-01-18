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
    void helper(TreeNode* root, int &k, int &ans){
        if(!root||k==0)return;
        helper(root->left, k, ans);
        k--;
        if(k==0)ans=root->val;
        helper(root->right, k, ans);
        return;
        
    }
    int kthSmallest(TreeNode* root, int k) {
        int ans;
        helper(root,k,ans);
        return ans;
    }
};

