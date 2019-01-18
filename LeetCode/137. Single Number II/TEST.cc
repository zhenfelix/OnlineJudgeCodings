
#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"

TEST_CASE("single number2", "singlenumber2")
{
    Solution s;
    
    std::vector<int> v1{2, 2, 3, 2};
    REQUIRE( (s.singleNumber(v1) == 3) );
    
    std::vector<int> v2{0,1,0,1,0,1,99};
    REQUIRE( (s.singleNumber(v2) == 99) );
}
