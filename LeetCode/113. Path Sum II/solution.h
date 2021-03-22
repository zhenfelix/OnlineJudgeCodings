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
    void dfs(TreeNode *root, int sum, vector<int> &tmp, vector<vector<int>> &ans){
        if(!root)return;
        tmp.push_back(root->val);
        if(!root->left && !root->right && root->val==sum){
            ans.push_back(tmp);
        }
        else{
            dfs(root->left, sum-root->val, tmp, ans);
            dfs(root->right, sum-root->val, tmp, ans);
        }
        tmp.pop_back();
        return;
    }
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> ans;
        vector<int> tmp;
        dfs(root, sum, tmp ,ans);
        return ans;
    }
};

class Solution {
public:
    void dfs(TreeNode* cur, int sums, vector<int> &path, vector<vector<int>> &res){
        path.push_back(cur->val);
        if(!cur->left && !cur->right){
            if(sums==cur->val){
                // vector<int> tmp = path;
                res.push_back(path);
            }
        }
        else{
            sums -= cur->val;
            if(cur->left)dfs(cur->left,sums,path,res);
            if(cur->right)dfs(cur->right,sums,path,res);
        }
        path.pop_back();
        return;
    }
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<int> path;
        vector<vector<int>> res;
        if(!root)return res;
        dfs(root,targetSum,path,res);
        return res;
    }
};


class Solution {
public:
    void dfs(TreeNode* cur, int sums, vector<int>* path, vector<vector<int>> &res){
        (*path).push_back(cur->val);
        if(!cur->left && !cur->right){
            if(sums==cur->val){
                // vector<int> tmp = path;
                res.push_back(*path);
            }
        }
        else{
            sums -= cur->val;
            if(cur->left)dfs(cur->left,sums,path,res);
            if(cur->right)dfs(cur->right,sums,path,res);
        }
        (*path).pop_back();
        return;
    }
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<int> path;
        vector<vector<int>> res;
        if(!root)return res;
        dfs(root,targetSum,&path,res);
        return res;
    }
};


class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> res;
        stack<TreeNode*> st;
        vector<int> path;
        int sums=0;
        if(!root)return res;
        st.push(root);

        TreeNode *last=root;
        while(!st.empty()){
            TreeNode *cur=st.top();
            // cout << cur->val << " " << sums << endl;
            if((!cur->left && !cur->right) || (cur->left==last || cur->right==last)){
                if(!cur->left && !cur->right){
                    sums += cur->val;
                    path.push_back(cur->val);
                    if(sums==targetSum)res.push_back(path);
                }
                sums -= cur->val;
                path.pop_back();
                st.pop();
                last=cur;
            }
            else{
                sums += cur->val;
                path.push_back(cur->val);
                if(cur->right)st.push(cur->right);
                if(cur->left)st.push(cur->left);
            }
        }
        return res;
    }
};