#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"

TEST_CASE("Remove Dup", "RemoveDup")
{
    Solution s;

    vector<int> v1{1,1,2};
    REQUIRE( (s.removeDuplicates(v1) == 2) );

    vector<int> v2{0,0,1,1,1,2,2,3,3,4};
    REQUIRE( (s.removeDuplicates(v2) == 5) );

//    vector<int> v3{-3, 4, 3, 90};
//    REQUIRE( (s.RemoveDup(v3, 0) == std::vector<int>{0, 2}) );
}
