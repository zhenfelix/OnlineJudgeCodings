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
    
    int next(stack<TreeNode*> &st){
        
        while(true){
            TreeNode *root=st.top();st.pop();
            if(!root->left && !root->right)return root->val;
            if(root->right)st.push(root->right);
            if(root->left)st.push(root->left);
        }
    }
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        stack<TreeNode*> st1,st2;
        if(root1)st1.push(root1);
        if(root2)st2.push(root2);
        while(!st1.empty() && !st2.empty()){
            if(next(st1)!=next(st2))return false;
        }
        return st1.empty() && st2.empty();
    }
};