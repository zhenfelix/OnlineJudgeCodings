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
    vector<int> ans;
    TreeNode *target;
    int K;
    vector<int> distanceK(TreeNode* root, TreeNode* target, int K) {
        this->target = target;
        this->K = K;
        dfs(root);
        return ans;
    }



    // Return vertex distance from node to target if exists, else -1
    // Vertex distance: the number of vertices on the path from node to target
    int dfs(TreeNode *node) {
        if (node == NULL)
            return -1;
        else if (node == target) {
            subtree_add(node, 0);
            return 0;
        } else {
            int L = dfs(node->left), R = dfs(node->right);
            if (L != -1) {
                if (L+1 == K) ans.push_back(node->val);
                subtree_add(node->right, L + 2);
                return L + 1;
            } else if (R != -1) {
                if (R+1 == K) ans.push_back(node->val);
                subtree_add(node->left, R + 2);
                return R + 1;
            } else {
                return -1;
            }
        }
    }

    // Add all nodes 'K - dist' from the node to answer.
    void subtree_add(TreeNode *node, int dist) {
        if (node == NULL) return;
        if (dist == K)
            ans.push_back(node->val);
        else {
            subtree_add(node->left, dist + 1);
            subtree_add(node->right, dist + 1);
        }
    }
};