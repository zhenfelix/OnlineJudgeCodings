
#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"

TEST_CASE("test", "test")
{
    Solution s;
    
    
    vector<int> v1{1,2,3,0,0,0};
    vector<int> t1{2,5,6};
    vector<int> ans1{1,2,2,3,5,6};
    s.merge(v1,3,t1,3);
    REQUIRE( (v1 == ans1) );

   


    
//    vector<int> v2{4,3,2,1};
//    vector<int> t2{4,3,2,2};
//    REQUIRE( (s.plusOne(v2) == t2) );
//    
//    vector<int> v3{9,9};
//    vector<int> t3{1,0,0};
//    REQUIRE( (s.plusOne(v3) == t3) );
}
