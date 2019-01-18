
#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"


TEST_CASE("test", "test")
{
    Solution s;
    
    
    string v1="A man, a plan, a canal: Panama";
    string t1="amanaP :lanac a ,nalp a ,nam A";
    REQUIRE( (s.reverseString(v1) == t1) );

    string v2="r";
    REQUIRE( (s.reverseString(v2) == v2) );
    
    string v3="";
    REQUIRE( (s.reverseString(v3) == v3) );

}
