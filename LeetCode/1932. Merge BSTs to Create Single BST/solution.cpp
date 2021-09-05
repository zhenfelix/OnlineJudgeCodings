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

const int inf = 0x3f3f3f3f;

class Solution
{
public:
    TreeNode *canMerge(vector<TreeNode *> &trees)
    {
        int n = trees.size();
        map<int, int> mp, cnt;
        for (int i = 0; i < n; i++)
        {
            mp[trees[i]->val] = i;
        }
        for (int i = 0; i < n; i++)
        {
            auto root = trees[i];
            if (root->left && mp.count(root->left->val))
                cnt[mp[root->left->val]]++;
            if (root->right && mp.count(root->right->val))
                cnt[mp[root->right->val]]++;
        }
        TreeNode *root = nullptr;
        vector<bool> used(n, false);
        for (int i = 0; i < n; i++)
        {
            if (cnt[i] == 0)
            {
                if (root)
                    return nullptr;
                root = trees[i];
            }
        }
        if (!root)
            return nullptr;

        if (!dfs(root, -inf, inf, used, mp, trees))
            return nullptr;

        for (int i = 0; i < n; i++)
            if (!used[i])
                return nullptr;
        return root;
    }
    bool dfs(TreeNode *cur, int lo, int hi, vector<bool> &used, map<int, int> &mp, vector<TreeNode *> &trees)
    {
        if (cur->val <= lo || cur->val >= hi)
            return false;
        if (!mp.count(cur->val))
            return true;
        if (used[mp[cur->val]])
            return false;
        used[mp[cur->val]] = true;
        if (cur->left)
        {
            if (mp.count(cur->left->val))
                cur->left = trees[mp[cur->left->val]];
            if (!dfs(cur->left, lo, cur->val, used, mp, trees))
                return false;
        }
        if (cur->right)
        {
            if (mp.count(cur->right->val))
                cur->right = trees[mp[cur->right->val]];
            if (!dfs(cur->right, cur->val, hi, used, mp, trees))
                return false;
        }
        return true;
    }
};