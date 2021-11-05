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
    TreeNode* removeLeafNodes(TreeNode* root, int target) {
        if (!root)
            return root;
        bool isleaf = true;
        if (root->left = removeLeafNodes(root->left, target))
            isleaf = false;
        if (root->right = removeLeafNodes(root->right, target))
            isleaf = false;
        if (isleaf && target == root->val)
            return nullptr;
        return root;
    }
};