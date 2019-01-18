
#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"


TEST_CASE("test", "test")
{
    Solution s;
    
    
    
    REQUIRE( s.hammingWeight(1)==1 );
    
    REQUIRE( s.hammingWeight(11)==3);
    
    REQUIRE( s.hammingWeight(128)==1 );

}
