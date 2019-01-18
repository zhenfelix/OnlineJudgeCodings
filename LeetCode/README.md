# LeetCode


### first commit


### unit test
- `g++ -std=c++11 TEST.cc` for c++ code under the unit test environment of catch2
- [example](https://github.com/catchorg/Catch2/blob/master/docs/tutorial.md#writing-tests)

```
// test.cpp
#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"

unsigned int Factorial( unsigned int number ) {
    return number <= 1 ? number : Factorial(number-1)*number;
}

TEST_CASE( "Factorials are computed", "[factorial]" ) {
    REQUIRE( Factorial(1) == 1 );
    REQUIRE( Factorial(2) == 2 );
    REQUIRE( Factorial(3) == 6 );
    REQUIRE( Factorial(10) == 3628800 );
}
```
