#include <vector>
#include <string>
#include <stack>
#include <map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        if(n==1||n==2)return n;
        vector<int> t;
        t.push_back(1);t.push_back(2);
        for(int i=2;i<n;i++){
            int a=t[i-1],b=t[i-2];
            t.push_back(a+b);
        }
        return t[n-1];
    }
};
