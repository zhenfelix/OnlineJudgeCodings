
#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"


TEST_CASE("test", "test")
{
    Solution s;
    
    
    vector<vector<int>> ans{{1},{1,1},{1,2,1},{1,3,3,1},{1,4,6,4,1}};
//    TreeNode *root1=createTree(v1, 0);
//    preorder(root1);
    REQUIRE( (s.generate(5) == ans) );

 
}
