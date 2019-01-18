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
    int depth(TreeNode* root, int &d){
        if(!root)return 0;
        int L=depth(root->left,d);
        int R=depth(root->right,d);
        d=max(d,L+R);
        return max(L,R)+1;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        int d=0;
        depth(root,d);
        return d;
    }
};