
#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"


TEST_CASE("test", "test")
{
    Solution s;
    
    
    vector<int> v1{0,1,0,3,12};
    vector<int> t1{1,3,12,0,0};
    s.moveZeroes(v1);
    REQUIRE( v1==t1 );
    
    vector<int> v2{0,1};
    vector<int> t2{1,0};
    s.moveZeroes(v2);
    REQUIRE( v2==t2 );
    
    vector<int> v3{0};
    vector<int> t3{0};
    s.moveZeroes(v3);
    REQUIRE( v3==t3 );

    vector<int> v4{};
    vector<int> t4{};
    s.moveZeroes(v4);
    REQUIRE( v4==t4 );
    
    vector<int> v5{0,0,1};
    vector<int> t5{1,0,0};
    s.moveZeroes(v5);
    REQUIRE( v5==t5 );
    
    vector<int> v6{1,0,0};
    vector<int> t6{1,0,0};
    s.moveZeroes(v6);
    REQUIRE( v6==t6 );

}
