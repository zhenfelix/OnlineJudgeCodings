#include <vector>
#include <string>
#include <queue>
#include <map>
#include <stack>
#include <algorithm>
using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int cc=0;
        while(n){
            if(n%2==1)cc++;
            n=n>>1;
        }
        return cc;
    }
};
