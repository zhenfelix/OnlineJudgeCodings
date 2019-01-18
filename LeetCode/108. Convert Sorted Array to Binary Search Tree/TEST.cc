
#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"

TreeNode *createTree(vector<int> v, int i)
{
    if(i>=v.size()||v[i]==-1)return NULL;
    TreeNode *root = new TreeNode(v[i]);
    root->left=createTree(v, 2*(i+1)-1);
    root->right=createTree(v, 2*(i+1));
    return root;
}

//void preorder(TreeNode* root){
//    if(root==NULL)return;
//    printf("%d ",root->val);
//    preorder(root->left);
//    preorder(root->right);
//}

bool Judge(TreeNode *root){
    if(root==NULL)return true;
    if(root->left!=NULL&&root->left->val>root->val)return false;
    if(root->right!=NULL&&root->right->val<root->val)return false;
    if(!Judge(root->left))return false;
    if(!Judge(root->right))return false;
    return true;
}

TEST_CASE("test", "test")
{
    Solution s;
    
    
    vector<int> v1{-10,-3,0,5,9};
//    TreeNode *root1=createTree(v1, 0);
//    preorder(root1);
    REQUIRE( (Judge(s.sortedArrayToBST(v1)) == true) );

    vector<int> v2{-3};
    //    TreeNode *root1=createTree(v1, 0);
    //    preorder(root1);
    REQUIRE( (Judge(s.sortedArrayToBST(v2)) == true) );
   
    vector<int> v3{-3,2,7,10};
    //    TreeNode *root1=createTree(v1, 0);
    //    preorder(root1);
    REQUIRE( (Judge(s.sortedArrayToBST(v3)) == true) );
    
    
    vector<int> v5{-3,2,2,2};
    //    TreeNode *root1=createTree(v1, 0);
    //    preorder(root1);
    REQUIRE( (Judge(s.sortedArrayToBST(v5)) == true) );
    
    vector<int> v4{};
    //    TreeNode *root1=createTree(v1, 0);
    //    preorder(root1);
    REQUIRE( (Judge(s.sortedArrayToBST(v4)) == true) );
    
    vector<int> v6{1,2,2,3,4,4,3};
    //    TreeNode *root1=createTree(v1, 0);
    //    preorder(root1);
    REQUIRE( (Judge(createTree(v6, 0)) == false) );
    
}
