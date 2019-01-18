
#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"

TEST_CASE("test", "test")
{
    Solution s;
    
    
    int n1=1;
    REQUIRE( (s.countAndSay(n1) == "1") );
    
    int n2=4;
    REQUIRE( (s.countAndSay(n2) == "1211") );
    
}
