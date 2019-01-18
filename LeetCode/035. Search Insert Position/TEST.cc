#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"

TEST_CASE("Remove Dup", "RemoveDup")
{
    Solution s;

    vector<int> v1{1,3,5,6};
    REQUIRE( (s.searchInsert(v1,5) == 2) );

    vector<int> v2{1,3,5,6};
    REQUIRE( (s.searchInsert(v2,2) == 1) );
    
    vector<int> v3{1,3,5,6};
    REQUIRE( (s.searchInsert(v3,7) == 4) );
    
    vector<int> v4{1,3,5,6};
    REQUIRE( (s.searchInsert(v4,0) == 0) );
//    vector<int> v3{-3, 4, 3, 90};
//    REQUIRE( (s.RemoveDup(v3, 0) == std::vector<int>{0, 2}) );
}
