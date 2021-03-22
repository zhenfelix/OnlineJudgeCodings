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
    void inorder(TreeNode *root, vector<int> &ans){
        if(root==NULL)return;
        inorder(root->left,ans);
        ans.push_back(root->val);
        inorder(root->right,ans);
        return;
    }
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ans;
        inorder(root,ans);
        return ans;
    }
};


class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        std::vector<int> res;
        stack<TreeNode*> st;
        TreeNode* cur=root;
        while(!st.empty() || cur){
            if(cur){
                // cout<<cur->val<<endl;
                
                st.push(cur);
                cur=cur->left;
            }
            else{
                // cout<<"null"<<st.top()->val<<endl;
                cur=st.top();
                res.push_back(cur->val);
                st.pop();
                cur=cur->right;
            }
        }
        return res;
    }
};

// Morris
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        std::vector<int> res;
        TreeNode* cur=root;
        while(cur){
            if(cur->left){
                TreeNode *right=cur->left;
                while(right->right && right->right!=cur)right=right->right;
                if(!right->right){
                    right->right=cur;
                    cur=cur->left;
                }
                else{
                    right->right=nullptr;
                    res.push_back(cur->val);
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