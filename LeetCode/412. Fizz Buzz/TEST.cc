
#define CATCH_CONFIG_MAIN
#include "../Catch/single_include/catch.hpp"
#include "solution.h"


TEST_CASE("test", "test")
{
    Solution s;
    
    
    vector<string> v1{"1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"};
    REQUIRE( (s.fizzBuzz(15) == v1) );


}
