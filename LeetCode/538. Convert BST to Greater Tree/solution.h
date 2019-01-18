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
//     void helper(TreeNode* root, int &psum, int &csum){
//         if(!root){
//             csum=psum,psum=0;
//             return;
//         }
//         helper(root->right,psum,csum);
//         root->val+=csum+psum;
//         csum=0;
//         psum=root->val;
//         helper(root->left,psum,csum);
//         return;
//     }
//     TreeNode* convertBST(TreeNode* root) {
//         int psum=0,csum=0;
//         helper(root,psum,csum);
//         return root;
//     }
// };

class Solution {
public:
    void helper(TreeNode* root, int &sum){
        if(!root)return;
        helper(root->right,sum);
        root->val+=sum;
        sum=root->val;
        helper(root->left,sum);
        return;
    }
    TreeNode* convertBST(TreeNode* root) {
        int sum=0;
        helper(root,sum);
        return root;
    }
};