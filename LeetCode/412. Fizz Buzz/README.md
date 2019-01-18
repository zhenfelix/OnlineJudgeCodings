`std::to_string(int n)`

```c++
class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> res;
        for( int i = 1, fizz = 0, buzz = 0; i <= n; i++){
            fizz++, buzz++;
            if( fizz == 3 && buzz == 5){
                res.push_back("FizzBuzz");
                fizz = buzz = 0;    
            }
            else if( fizz == 3){
                res.push_back("Fizz");
                fizz = 0;
            }
            else if( buzz == 5){
                res.push_back("Buzz");
                buzz =0;
            }
            else
                res.push_back(to_string(i));
        }
        return res;
    }
};
```
