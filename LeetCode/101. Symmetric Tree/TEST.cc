
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

void preorder(TreeNode* root){
    if(root==NULL)return;
    printf("%d ",root->val);
    preorder(root->left);
    preorder(root->right);
}

TEST_CASE("test", "test")
{
    Solution s;
    
    
    vector<int> v1{1,2,2,3,4,4,3};
    TreeNode *root1=createTree(v1, 0);
//    preorder(root1);
    REQUIRE( (s.isSymmetric(root1) == true) );

    
    vector<int> v2{1,2,2,-1,3,-1,3};
    TreeNode *root2=createTree(v2, 0);
//    preorder(root2);
    REQUIRE( (s.isSymmetric(root2) == false) );
    
    vector<int> v3{};
    TreeNode *root3=createTree(v3, 0);
    //    preorder(root2);
    REQUIRE( (s.isSymmetric(root3) == true) );
}
