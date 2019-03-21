/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
// class Solution {
// public:
//     pair<TreeNode*,TreeNode*> dfs(TreeNode* root){
//         // if(root->left==NULL && root->right==NULL)return make_pair(root,root);
//         TreeNode *l,*r;
//         if(root->left==NULL)l=root;
//         else{
//             pair<TreeNode*,TreeNode*> tmp=dfs(root->left);
//             l=tmp.first;
//             tmp.second->right=root;
//         }
//         if(root->right==NULL)r=root;
//         else{
//             pair<TreeNode*,TreeNode*> tmp=dfs(root->right);
//             r=tmp.second;
//             root->right=tmp.first;
//         }
//         root->left=NULL;
//         return make_pair(l,r);
//     }
//     TreeNode* increasingBST(TreeNode* root) {
//         if(!root)return root;
//         pair<TreeNode*,TreeNode*> ans=dfs(root);
//         return ans.first;
//     }
// };


class Solution {
public:
    TreeNode* cur;
    void inorder(TreeNode* root){
        if(!root)return;
        inorder(root->left);
        cur->right=root;
        root->left=NULL;
        cur=root;
        inorder(root->right);
        return;
    }
    TreeNode* increasingBST(TreeNode* root) {
        TreeNode* ans=new TreeNode(0);
        cur=ans;
        inorder(root);
        return ans->right;
    }
};