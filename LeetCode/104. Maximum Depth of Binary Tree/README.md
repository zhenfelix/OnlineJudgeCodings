another solution
```c++
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
    int maxDepth(TreeNode* root) {
        int i = trace(root);
        return i;
    }

    int trace(TreeNode* node){
        if(node == NULL) return 0;
        int left = trace(node->left);
        int right = trace(node->right);
        int max = left > right ? left : right;
        return 1+max;
    }
};
```
