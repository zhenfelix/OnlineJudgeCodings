build tree from array
```c++
TreeNode *createTree(vector<int> v, int i)
{
    if(i>=v.size()||v[i]==-1)return NULL;
    TreeNode *root = new TreeNode(v[i]);
    root->left=createTree(v, 2*(i+1)-1);
    root->right=createTree(v, 2*(i+1));
    return root;
}

void preorder(TreeNode* root){
    if(root==NULL)return;
    printf("%d ",root->val);
    preorder(root->left);
    preorder(root->right);
}
```

compare while building mirrior
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
private:
    bool mirror(TreeNode *a, TreeNode *b) {
        if (a == NULL && b == NULL)
            return true;
        if (a == NULL || b == NULL)
            return false;
        if (a->val != b->val)
            return false;
        if (!mirror(a->left, b->right))
            return false;
        if (!mirror(a->right, b->left))
            return false;
        return true;
    }

public:
    bool isSymmetric(TreeNode* root) {
        if (root == NULL)
            return true;
        return mirror(root->left, root->right);
    }
};
```
