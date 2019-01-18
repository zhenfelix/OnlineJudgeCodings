
#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"


TEST_CASE("test", "test")
{
    Solution s;
    
    
    vector<int> v1{1,2,3,4,5,6,7};
    vector<int> t1{5,6,7,1,2,3,4};
    s.rotate(v1,3);
    REQUIRE( v1==t1 );
   
    
    vector<int> v2{1};
    vector<int> t2{1};
    s.rotate(v2,0);
    REQUIRE( v2==t2 );
    
    vector<int> v3{1};
    vector<int> t3{1};
    s.rotate(v3,1);
    REQUIRE( v3==t3 );
    
    
    vector<int> v4{1,2};
    vector<int> t4{2,1};
    s.rotate(v4,3);
    REQUIRE( v4==t4 );
}
