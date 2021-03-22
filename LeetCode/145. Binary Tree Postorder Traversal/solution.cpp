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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> st;
        if(!root)return res;
        st.push(root);
        TreeNode *last=root;
        while(!st.empty()){
            TreeNode *cur=st.top();
            if((!cur->left && !cur->right) || (cur->left==last || cur->right==last)){
                st.pop();
                last=cur;
                res.push_back(cur->val);
            }
            else{
                if(cur->right)st.push(cur->right);
                if(cur->left)st.push(cur->left);
            }
        }
        return res;
    }
};