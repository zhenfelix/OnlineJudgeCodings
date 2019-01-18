#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"

TEST_CASE("Remove Dup", "RemoveDup")
{
    Solution s;

    vector<int> v1{3,2,2,3};
    REQUIRE( (s.removeElement(v1,3) == 2) );

    vector<int> v2{0,1,2,2,3,0,4,2};
    REQUIRE( (s.removeElement(v2,2) == 5) );

//    vector<int> v3{-3, 4, 3, 90};
//    REQUIRE( (s.RemoveDup(v3, 0) == std::vector<int>{0, 2}) );
}
