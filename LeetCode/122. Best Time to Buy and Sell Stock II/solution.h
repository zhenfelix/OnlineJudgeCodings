#include <vector>
#include <string>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans=0;
        int len=prices.size();//vector.size() aka unsigned long 
        for(int i=0;i<len-1;i++){
            int b=prices[i+1],a=prices[i];
            if(b-a>0)ans=ans+(b-a);
        }
        return ans;
    }
};
