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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        vector<TreeNode*> q, nq;
        if (root) q.push_back(root);
        while (!q.empty()){
            int n = q.size();
            nq.clear();
            for (int i = 0; i < n; i++){
                TreeNode *cur = q[i];
                if (i == n-1) res.push_back(cur->val);
                if (cur->left) nq.push_back(cur->left);
                if (cur->right) nq.push_back(cur->right);
            }
            swap(q,nq);
        }
        return res;
    }
};