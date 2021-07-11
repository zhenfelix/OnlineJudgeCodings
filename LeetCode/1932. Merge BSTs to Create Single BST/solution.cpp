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
const int N = 50005;
int cnt = 0;

bool valid(TreeNode* root, int lower, int upper) {
    if (!root)
        return true;
    cnt++;
    if (root->val < lower || root->val > upper)
        return false;
    return valid(root->left, lower, root->val - 1) && valid(root->right, root->val + 1, upper);
}

class Solution {
public:
    TreeNode* canMerge(vector<TreeNode*>& trees) {
        int n = trees.size();
        vector<TreeNode*> parent(N, nullptr);
        int tot = 0;
        for (TreeNode *tree : trees) {
            tot++;
            
            if (tree->left) {
                tot++;
                if (parent[tree->left->val])
                    return nullptr;
                parent[tree->left->val] = tree;
            }
            
            if (tree->right) {
                tot++;
                if (parent[tree->right->val])
                    return nullptr;
                parent[tree->right->val] = tree;
            }
        }
        
        TreeNode *root = nullptr;
        for (TreeNode *tree : trees) {
            if (!parent[tree->val]) {
                if (root)
                    return nullptr;
                root = tree;
            } else {
                TreeNode *p = parent[tree->val];
                if (p->val > tree->val)
                    p->left = tree;
                else
                    p->right = tree;
            }
        }

        cnt = 0;
        if (valid(root, 1, N) && cnt == tot + 1 - n)
            return root;
        
        return nullptr;
    }
};


// 作者：吴自华
// 链接：https://leetcode-cn.com/circle/discuss/U8tCN1/view/pb75qx/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。