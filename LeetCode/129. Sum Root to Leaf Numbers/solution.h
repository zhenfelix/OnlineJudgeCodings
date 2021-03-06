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


//     int sums(vector<int> vecs){
//         int s=0;
//         for(auto v: vecs){
//             s=s*10+v;
//         }
//         return s;
//     }
//     void dfs (TreeNode *root, vector<int> &tmp, int &ans){
//         if(!root)return;
//         tmp.push_back(root->val);
//         if(!root->left && !root->right){
//             ans+=sums(tmp);
//         }
//         else{
//             dfs(root->left, tmp, ans);
//             dfs(root->right, tmp, ans);
//         }
//         tmp.pop_back();
//         return;
//     }
//     int sumNumbers (TreeNode* root) {
//         int ans=0;
//         vector<int> tmp;
//         dfs(root, tmp ,ans);
//         return ans;
//     }
// };

class Solution {
public:
    int ans = 0;
    void dfs(TreeNode* node, int number){
        number = number * 10 + node->val;
        if(node->left == NULL && node->right == NULL){
            ans += number;
        }
        if(node->left != NULL)
            dfs(node->left, number);
        if(node->right != NULL)
            dfs(node->right, number);
    }
    int sumNumbers(TreeNode* root) {
        if(root == NULL)
            return ans;
        int number = 0;
        dfs(root, number);
        return ans;
    }
};

class Solution {
public:
    int sumNumbers(TreeNode* root) {
        int res = 0;
        dfs(root,0,res);
        return res;
    }
    void dfs(TreeNode* root, int sum, int &res){
        if(!root)return;
        sum *= 10;
        sum += root->val;
        if(!root->left && !root->right)res += sum;
        dfs(root->left,sum,res);
        dfs(root->right,sum,res);
        return;
    }
};