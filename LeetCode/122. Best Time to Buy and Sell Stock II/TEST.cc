
#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"


TEST_CASE("test", "test")
{
    Solution s;
    
    
    vector<int> v1{7,1,5,3,6,4};
//    TreeNode *root1=createTree(v1, 0);
//    preorder(root1);
    REQUIRE( (s.maxProfit(v1) == 7) );

    vector<int> v2{7,6,4,3,1};
    //    TreeNode *root1=createTree(v1, 0);
    //    preorder(root1);
    REQUIRE( (s.maxProfit(v2) == 0) );
    
    vector<int> v3{1,2,3,4,5};
    //    TreeNode *root1=createTree(v1, 0);
    //    preorder(root1);
    REQUIRE( (s.maxProfit(v3) == 4) );
    
    vector<int> v4{};
    //    TreeNode *root1=createTree(v1, 0);
    //    preorder(root1);
    REQUIRE( (s.maxProfit(v4) == 0) );
    
    vector<int> v5{1};
    //    TreeNode *root1=createTree(v1, 0);
    //    preorder(root1);
    REQUIRE( (s.maxProfit(v5) == 0) );
 
}
