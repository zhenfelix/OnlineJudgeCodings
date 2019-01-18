// /**
//  * Definition for a binary tree node.
//  * struct TreeNode {
//  *     int val;
//  *     TreeNode *left;
//  *     TreeNode *right;
//  *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
//  * };
//  */
// class Solution {
// public:
//     vector<vector<int>> levelOrder(TreeNode* root) {
//         queue<TreeNode*> q;
//         queue<bool> bq;
//         vector<int> t;
//         vector<vector<int>> ans;
//         if(!root)return ans;
//         q.push(root);bq.push(true);
//         bool pre=true;
//         while(!q.empty()){
//             TreeNode *tmp=q.front();
//             bool cur=bq.front();
//             q.pop();bq.pop();
//             if(cur!=pre){
//                 ans.push_back(t);t.clear();
//             }
//             t.push_back(tmp->val);
//             pre=cur;
//             if(tmp->left!=NULL){
//                 q.push(tmp->left);bq.push(!cur);
//             }
//             if(tmp->right!=NULL){
//                 q.push(tmp->right);bq.push(!cur);
//             }
//         }
//         ans.push_back(t);
//         return ans;
//     }
// };


// class Solution {
// public:
//     vector<vector<int> > levelOrder(TreeNode *root) {
//         vector<vector<int> >  result;
//         if (!root) return result;
//         queue<TreeNode*> q;
//         q.push(root);
//         q.push(NULL);
//         vector<int> cur_vec;
//         while(!q.empty()) {
//             TreeNode* t = q.front();
//             q.pop();
//             if (t==NULL) {
//                 result.push_back(cur_vec);
//                 cur_vec.resize(0);
//                 if (q.size() > 0) {
//                     q.push(NULL);
//                 }
//             } else {
//                 cur_vec.push_back(t->val);
//                 if (t->left) q.push(t->left);
//                 if (t->right) q.push(t->right);
//             }
//         }
//         return result;
//     }
// };

// class Solution {
// public:
//     vector<vector<int>> levelOrder(TreeNode* root) {
//         if (!root) { return {}; }
//         vector<int> row;
//         vector<vector<int> > result;
//         queue<TreeNode*> q;
//         q.push(root);
//         int count = 1;

//             while (!q.empty()) {
//             if (q.front()->left) { q.push(q.front()->left); }
//             if (q.front()->right) { q.push(q.front()->right); }
//             row.push_back(q.front()->val), q.pop();
//             if (--count == 0) {
//                 result.emplace_back(row), row.clear();
//                 count = q.size();
//             }
//         }
//         return result;
//     }
// };

class Solution {
public:
    

void buildVector(TreeNode *root, int depth, vector<vector<int>> &ret)
{
    if(root == NULL) return;
    if(ret.size() == depth)
        ret.push_back(vector<int>());
    
    ret[depth].push_back(root->val);
    buildVector(root->left, depth + 1, ret);
    buildVector(root->right, depth + 1, ret);
}

vector<vector<int> > levelOrder(TreeNode *root) {
    vector<vector<int>> ret;
    buildVector(root, 0, ret);
    return ret;
}
};
