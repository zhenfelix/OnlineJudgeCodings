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
    TreeNode* helper(vector<int>& preorder, vector<int>& inorder, int i, int j, int m, int n){
        if(i>j)return NULL;
        TreeNode* root = new TreeNode(preorder[i]);
        int k=m;
        for(;k<=n;k++)if(inorder[k]==preorder[i])break;
        int left=k-m,right=n-k;
        root->left=helper(preorder,inorder,i+1,i+left,m,k-1);
        root->right=helper(preorder,inorder,i+left+1,j,k+1,n);
        return root;
    }
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int len=preorder.size();
        return helper(preorder,inorder,0,len-1,0,len-1);
    }
};