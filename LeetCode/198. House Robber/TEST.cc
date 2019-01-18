
#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"


TEST_CASE("test", "test")
{
    Solution s;
    
    
    vector<int> v1{1,2,3,1};
    REQUIRE( s.rob(v1)==4 );
    
    vector<int> v2{2,7,9,3,1};
    REQUIRE( s.rob(v2)==12 );
    
    vector<int> v3{4,2,5,9,3,1,8};
    REQUIRE( s.rob(v3)==21 );
    
    vector<int> v4{};
    REQUIRE( s.rob(v4)==0 );

}
