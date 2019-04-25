#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"



TEST_CASE("test", "test")
{
    Solution s;
 
    
    
    
    
    vector<double> nums1{8.02,7.43,4.57,5.39};
    vector<double> nums2{10.05,2.43};
//    vector<vector<int>> grid{{1},{1},{2},{1}};
//    vector<vector<int>> ans(4,vector<int>(0));
//    string str="aaabb";int k=3;

    
//    REQUIRE(s.solve(nums1,11)== 2.0);
    REQUIRE(s.solve(nums2,3)== 3.0);
    //    vector<int> v2{4,3,2,1};
    //    vector<int> t2{4,3,2,2};
    //    REQUIRE( (s.plusOne(v2) == t2) );
    //
    //    vector<int> v3{9,9};
    //    vector<int> t3{1,0,0};
    //    REQUIRE( (s.plusOne(v3) == t3) );
}
