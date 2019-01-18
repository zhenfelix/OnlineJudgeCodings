#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"

TEST_CASE("test", "test")
{
    Solution s;

    vector<string> v1{"flower","flow","flight"};
    REQUIRE( (s.longestCommonPrefix(v1) == "fl") );
    
    vector<string> v2{"dog","racecar","car"};
    REQUIRE( (s.longestCommonPrefix(v2) == "") );
    
    vector<string> v3{"dog","dog"};
    REQUIRE( (s.longestCommonPrefix(v3) == "dog") );
    
    vector<string> v4{"dog"};
    REQUIRE( (s.longestCommonPrefix(v4) == "dog") );
    
    vector<string> v5{};
    REQUIRE( (s.longestCommonPrefix(v5) == "") );

//
//    vector<int> v3{1,3,5,6};
//    REQUIRE( (s.searchInsert(v3,7) == 4) );

}
