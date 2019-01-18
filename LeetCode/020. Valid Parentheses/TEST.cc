#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"

TEST_CASE("test", "test")
{
    Solution s;

    string v1="()";
    REQUIRE( (s.isValid(v1) == true) );
    
    string v2="()[]{}";
    REQUIRE( (s.isValid(v2) == true) );

    string v3="(]";
    REQUIRE( (s.isValid(v3) == false) );
    
    string v4="([)]";
    REQUIRE( (s.isValid(v4) == false) );
    
    string v5="{[]}";
    REQUIRE( (s.isValid(v5) == true) );
    
    string v6="]";
    REQUIRE( (s.isValid(v6) == false) );
//
//    vector<int> v3{1,3,5,6};
//    REQUIRE( (s.searchInsert(v3,7) == 4) );

}
