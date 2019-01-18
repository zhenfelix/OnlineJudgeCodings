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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        stack<TreeNode*>left,right;
        vector<vector<int>> ans;
        vector<int> v;
        if(root)left.push(root);
        while(!left.empty()||!right.empty()){
                while(!left.empty()){
                TreeNode* tmp=left.top();left.pop();
                v.push_back(tmp->val);
                if(tmp->left!=NULL)right.push(tmp->left);
                if(tmp->right!=NULL)right.push(tmp->right);
                }
                if(v.size()>0)ans.push_back(v);v.clear();
                while(!right.empty()){
                TreeNode* tmp=right.top();right.pop();
                v.push_back(tmp->val);
                if(tmp->right!=NULL)left.push(tmp->right);
                if(tmp->left!=NULL)left.push(tmp->left);
                }
                if(v.size()>0)ans.push_back(v);v.clear();
        }
        return ans;
    }
};


// class Solution {
    
// private:    
//     void aux(TreeNode* cur, int level, vector<vector<int>> &solution) {
        
//         if (level == solution.size()) {
//             vector<int> blank;
//             solution.push_back(blank);
//         }
//         if (level%2 == 0) {
//             solution[level].push_back(cur->val);
//         }
//         else {
//             solution[level].insert(solution[level].begin(), cur->val);            
//         }
//         if (cur->left) {
//             aux(cur->left, level+1, solution);            
//         }
//         if (cur->right) {
//             aux(cur->right, level+1, solution);
//         }
//     }
    
    
// public:
//     vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        
//         vector<vector<int>> solution;
//         if (root) {
//             aux(root, 0, solution);
//         }
//         return solution;
        
//     }        
// };