
#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"

TEST_CASE("Two Sum", "twoSum")
{
    Solution s;
    
    string a1="hello";
    string b1="ll";
    REQUIRE( (s.strStr(a1,b1) == 2) );
    
    string a2="aaaaa";
    string b2="bba";
    REQUIRE( (s.strStr(a2,b2) == -1) );
    
    string a3="aaaaa";
    string b3="";
    REQUIRE( (s.strStr(a3,b3) == 0) );
    
}
