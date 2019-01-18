
#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"


TEST_CASE("test", "test")
{
    Solution s;
    
    
    vector<int> v1{4,1,-1,2,-1,2,3};
    vector<int> t1{-1,2};
    REQUIRE(s.topKFrequent(v1,2)==t1 );
   
    
    
}
