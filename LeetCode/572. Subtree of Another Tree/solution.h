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
//     bool equal(TreeNode* a, TreeNode* b){
//         if(!a&&!b)return true;
//         if(!a||!b)return false;
//         if(a->val!=b->val)return false;
//         return equal(a->left,b->left)&&equal(a->right,b->right);
//     }
//     bool isSubtree(TreeNode* s, TreeNode* t) {
//         if(!s)return equal(s,t);
//         return equal(s,t)||isSubtree(s->left,t)||isSubtree(s->right,t);
//     }
// };

class Solution {
public:
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if(s == nullptr) return t == nullptr;
        return isSame(s,t) | isSubtree(s->left, t) | isSubtree(s->right, t);
    }
    bool isSame(TreeNode *s, TreeNode *t)
    {
        if(s == nullptr || t == nullptr) return s == t;
        return s->val == t->val && isSame(s->left, t->left) && isSame(s->right, t->right);
    }
};