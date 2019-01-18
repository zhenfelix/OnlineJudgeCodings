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
    TreeNode* helper(TreeNode* root){
        if(!root)return NULL;
        if(root->left==NULL&&root->right==NULL)return root;
        TreeNode *tmp=root->right;
        TreeNode *end;
        if(root->left!=NULL){
            end=helper(root->left);
            root->right=root->left;
            end->right=tmp;
            root->left=NULL;end->left=NULL;
        }
        if(tmp!=NULL)return helper(tmp);
        return end;
    }
    void flatten(TreeNode* root) {
        TreeNode* dummy=helper(root);
        return;
    }
};