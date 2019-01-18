#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"



TEST_CASE("test", "test")
{
    Solution s;
    
    
    //    vector<int> v1{1,2,3};
    //    vector<int> t1{1,2,4};
//    REQUIRE( (s.mySqrt(1) == 1) );
//
//    REQUIRE( (s.mySqrt(4) == 2) );
//
//    REQUIRE( (s.mySqrt(8) == 2) );
//    vector<int> v{3,2,3,1,2,4,5,5,6};
    vector<int> nums{1,1,2};
    vector<vector<int>> ans{{1,1,2},{1,2,1},{2,1,1}};
    REQUIRE( (s.permuteUnique(nums))==ans);
    
    
    //    vector<int> v2{4,3,2,1};
    //    vector<int> t2{4,3,2,2};
    //    REQUIRE( (s.plusOne(v2) == t2) );
    //
    //    vector<int> v3{9,9};
    //    vector<int> t3{1,0,0};
    //    REQUIRE( (s.plusOne(v3) == t3) );
}
