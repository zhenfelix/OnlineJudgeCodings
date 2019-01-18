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
//     void helper(TreeNode* root, vector<int> &ans){
//         if(!root)return;
//         ans.push_back(root->val);
//         helper(root->left,ans);
//         helper(root->right,ans);
//         return;
//     }
//     vector<int> preorderTraversal(TreeNode* root) {
//         vector<int> ans;
//         helper(root,ans);
//         return ans;
//     }
// };

class Solution {
public:

    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        stack<TreeNode*> st;
        if(!root)return ans;
        st.push(root);
        while(!st.empty()){
            TreeNode* tmp=st.top();st.pop();
            ans.push_back(tmp->val);
            if(tmp->right!=NULL)st.push(tmp->right);
            if(tmp->left!=NULL)st.push(tmp->left);
        }
        return ans;
    }
};