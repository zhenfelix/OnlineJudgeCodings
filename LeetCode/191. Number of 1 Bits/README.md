bit operations
```c++
class Solution {
public:
    int hammingWeight(uint32_t n) {
        uint32_t mask=1;
        int res=0;
        while (n){
            uint32_t tmp=mask&n;
            if (tmp){
                res++;
            }
            n>>=1;
        }
        return res;
    }
};
```
