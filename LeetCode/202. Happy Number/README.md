similar to the solution of cyclic linked list solution, with the help of two pointers
```c++
class Solution {
public:
    bool isHappy(int n) {
        if (n < 0) return false;

        int tort = g(n);
        int hare = g(g(n));
        while (tort != 1 && tort != hare)
        {
            tort = g(tort);
            hare = g(g(hare));
        }
        return tort == 1 ? true : false;
    }

    int g(int n)
    {
        int result = 0;
        while (n)
        {
            result += (n % 10) * (n % 10);
            n /= 10;
        }
        return result;
    }
};
```
