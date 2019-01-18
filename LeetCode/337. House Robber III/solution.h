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
//     vector<TreeNode*> postorder(TreeNode* root){
//         if(!root){
//             vector<TreeNode*> ans(2);
//             ans[0]=new TreeNode(0);ans[1]=new TreeNode(0);
//             return ans;
//         }
//         vector<TreeNode*> left=postorder(root->left);
//         vector<TreeNode*> right=postorder(root->right);
//         vector<TreeNode*> ans(2);
//         int tmp=0;
//         // tmp=max(tmp,left[0]->val+right[0]->val);tmp=max(tmp,left[1]->val+right[1]->val);
//         // tmp=max(tmp,left[0]->val+right[1]->val);tmp=max(tmp,left[1]->val+right[0]->val);
//         ans[0]=new TreeNode(root->val+left[1]->val+right[1]->val);
//         left[0]->val=max(left[0]->val,left[1]->val);
//         right[0]->val=max(right[0]->val,right[1]->val);
//         ans[1]=new TreeNode(left[0]->val+right[0]->val);
//         return ans;
//     }
//     int rob(TreeNode* root) {
//         vector<TreeNode*> ans=postorder(root);
//         return max(ans[0]->val,ans[1]->val);
//     }
// };

class Solution {
public:
    vector<int> postorder(TreeNode* root){
        if(!root){
            vector<int> ans(2,0);
            return ans;
        }
        vector<int> left=postorder(root->left);
        vector<int> right=postorder(root->right);
        vector<int> ans(2);
        int tmp=0;
        // tmp=max(tmp,left[0]->val+right[0]->val);tmp=max(tmp,left[1]->val+right[1]->val);
        // tmp=max(tmp,left[0]->val+right[1]->val);tmp=max(tmp,left[1]->val+right[0]->val);
        ans[0]=root->val+left[1]+right[1];
        left[0]=max(left[0],left[1]);
        right[0]=max(right[0],right[1]);
        ans[1]=left[0]+right[0];
        return ans;
    }
    int rob(TreeNode* root) {
        vector<int> ans=postorder(root);
        return max(ans[0],ans[1]);
    }
};