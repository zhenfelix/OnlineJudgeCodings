
#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"


TEST_CASE("test", "test")
{
    Solution s;
    
    
    vector<int> v1{7,1,5,3,6,4};
//    TreeNode *root1=createTree(v1, 0);
//    preorder(root1);
    REQUIRE( (s.maxProfit(v1) == 5) );

    vector<int> v2{7,6,4,3,1};
    //    TreeNode *root1=createTree(v1, 0);
    //    preorder(root1);
    REQUIRE( (s.maxProfit(v2) == 0) );
 
}
