    #include <vector>
#include <string>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// // class Solution {
// public:
//     void Mirrior(TreeNode* &s, TreeNode* &t){
//         if(s==NULL)return;
//         if(s->right!=NULL)t->left=new TreeNode(s->right->val);
//         if(s->left!=NULL)t->right=new TreeNode(s->left->val);
//         Mirrior(s->right, t->left);
//         Mirrior(s->left,t->right);
//     }
//     bool TreeComp(TreeNode* &a, TreeNode* &b){
//         if(a==NULL||b==NULL){
//             if(a==NULL&&b==NULL)return true;
//             else return false;
//         }
//         else if(a->val!=b->val)return false;
//         else{
//             return TreeComp(a->left, b->left)&&TreeComp(a->right, b->right);
//         }
        
//     }
//     bool isSymmetric(TreeNode* root) {
//         TreeNode *mirrior;
//         if(root!=NULL)mirrior=new TreeNode(root->val);
//         else mirrior=NULL;
//         Mirrior(root, mirrior);
//         return TreeComp(root, mirrior);
//     }
// };


class Solution {
public:

    bool TreeComp(TreeNode* a, TreeNode* b){
        if(a==NULL||b==NULL){
            if(a==NULL&&b==NULL)return true;
            else return false;
        }
        else if(a->val!=b->val)return false;
        else{
            return TreeComp(a->left, b->right)&&TreeComp(a->right, b->left);
        }
        
    }
    bool isSymmetric(TreeNode* root) {
        if(root==NULL)return true;
        return TreeComp(root->left, root->right);
    }
};


// class Solution {
// public:
//     bool isSymmetric(TreeNode* root) {
//         if(!root) return true;
//         return compare(root->left, root->right);
//     }

// private:
//     bool compare(TreeNode *p1, TreeNode *p2) {
//         if(!p1 && !p2) return true;
//         if(!p1 || !p2) return false;
//         if(p1->val != p2->val) return false;
//         return compare(p1->left, p2->right) && compare(p1->right, p2->left);
//     }
// };


// class Solution {
// public:
//     bool isSymmetric(TreeNode* root) {
//         TreeNode *left, *right;
//         if(!root) return true;
//         queue<TreeNode*> q;
//         q.push(root->left);
//         q.push(root->right);
//         while(!q.empty()) {
//             left=q.front();
//             q.pop();
//             right=q.front();
//             q.pop();
//             if(left==NULL && right==NULL)
//                 continue;
//             if(left==NULL || right==NULL)
//                 return false;
//             if(left->val!=right->val)
//                 return false;
//             q.push(left->left);
//             q.push(right->right);
//             q.push(left->right);
//             q.push(right->left);
//         }
//         return true;
//     }
// };