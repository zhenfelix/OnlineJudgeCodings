#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"

TEST_CASE("Remove Dup", "RemoveDup")
{
    Solution s;

    
    string v1="III";
    REQUIRE( (s.romanToInt(v1) == 3) );
    
    string v2="IV";
    REQUIRE( (s.romanToInt(v2) == 4) );
    
    string v3="IX";
    REQUIRE( (s.romanToInt(v3) == 9) );
    
    string v4="LVIII";
    REQUIRE( (s.romanToInt(v4) == 58) );
    
    string v5="MCMXCIV";
    REQUIRE( (s.romanToInt(v5) == 1994) );
//
//    vector<int> v3{1,3,5,6};
//    REQUIRE( (s.searchInsert(v3,7) == 4) );

}
