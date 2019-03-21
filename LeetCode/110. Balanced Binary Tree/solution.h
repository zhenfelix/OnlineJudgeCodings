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
//     void dfs(TreeNode* root, int &h, bool &flag){
//         if(!root){
//             h=0;
//             flag=true;
//             return;
//         }
//         int l,r;
//         bool lf,rf;
//         dfs(root->left,l,lf);
//         dfs(root->right,r,rf);
//         h=max(l,r)+1;
//         if(lf&&rf&&(abs(l-r)<=1)){
//             flag=true;
//             return;
//         }
//         flag=false;
//         return;
//     }
//     bool isBalanced(TreeNode* root) {
//         bool flag=false;
//         int h;
//         dfs(root, h, flag);
//         return flag;
//     }
// };

class solution {
public:
int dfsHeight (TreeNode *root) {
        if (root == NULL) return 0;
        
        int leftHeight = dfsHeight (root -> left);
        if (leftHeight == -1) return -1;
        int rightHeight = dfsHeight (root -> right);
        if (rightHeight == -1) return -1;
        
        if (abs(leftHeight - rightHeight) > 1)  return -1;
        return max (leftHeight, rightHeight) + 1;
    }
    bool isBalanced(TreeNode *root) {
        return dfsHeight (root) != -1;
    }
};