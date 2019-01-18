
#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"


TEST_CASE("test", "test")
{
    Solution s;
    
    
    string v1="A man, a plan, a canal: Panama";
    REQUIRE( (s.isPalindrome(v1) == true) );

    string v2="race a car";
    REQUIRE( (s.isPalindrome(v2) == false) );
    
    string v3="0P";
    REQUIRE( (s.isPalindrome(v3) == false) );

}
