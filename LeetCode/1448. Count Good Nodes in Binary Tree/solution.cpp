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
    int goodNodes(TreeNode* root, int mx = INT_MIN) {
        if (!root)
            return 0;
        int cnt = root->val >= mx ? 1 : 0;
        mx = max(mx, root->val);
        cnt += goodNodes(root->left, mx);
        cnt += goodNodes(root->right, mx);
        return cnt;
    }
};