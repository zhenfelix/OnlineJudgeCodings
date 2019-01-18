/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
// class Solution {
// public:
//     void helper(TreeLinkNode *root){
//         if(!root->left)return;
//         root->left->next=root->right;
//         if(!root->next)root->right->next=NULL;
//         else root->right->next=root->next->left;
//         helper(root->left);
//         helper(root->right);
//         return;
//     }
//     void connect(TreeLinkNode *root) {
//         if(!root)return;
//         root->next=NULL;
//         helper(root);
//         return;
//     }
// };

// class Solution {
// public:

//     // recursive solution
//     void connect(TreeLinkNode *root){
//         if(!root||!root->left) return;
        
//         root->left->next = root->right;
//         if(root->next) root->right->next = root->next->left;
//         connect(root->left);
//         connect(root->right);
//     }
// };

//iterative, real O(1) space
class Solution {
public:

    // recursive solution
    void connect(TreeLinkNode *root){
        TreeLinkNode *start=root;
        while(start){
            TreeLinkNode *level=start;
            while(level&&level->left){
                level->left->next=level->right;
                if(level->next)level->right->next=level->next->left;
                level=level->next;
            }
            start=start->left;
        }
        return;
    }
};