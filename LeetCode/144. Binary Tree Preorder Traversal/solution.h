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
        vector<int> res;
        stack<TreeNode*> st;
        if(root)st.push(root);
        while(!st.empty()){
            TreeNode* cur=st.top();
            st.pop();
            res.push_back(cur->val);
            if(cur->right)st.push(cur->right);
            if(cur->left)st.push(cur->left);
        }
        return res;
    }
};


class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        std::vector<int> res;
        stack<TreeNode*> st;
        TreeNode* cur=root;
        while(!st.empty() || cur){
            if(cur){
                // cout<<cur->val<<endl;
                res.push_back(cur->val);
                st.push(cur);
                cur=cur->left;
            }
            else{
                // cout<<"null"<<st.top()->val<<endl;
                cur=st.top()->right;
                st.pop();
            }
        }
        return res;
    }
};

// Morris
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        std::vector<int> res;
        TreeNode* cur=root;
        while(cur){
            if(cur->left){
                TreeNode *right=cur->left;
                while(right->right && right->right!=cur)right=right->right;
                if(!right->right){
                    res.push_back(cur->val);
                    right->right=cur;
                    cur=cur->left;
                }
                else{
                    right->right=nullptr;
                    cur=cur->right;
                }
            }
            else{
                res.push_back(cur->val);
                cur=cur->right;
            }
        }
        return res;
    }
};