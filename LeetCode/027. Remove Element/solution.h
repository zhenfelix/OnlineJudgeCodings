#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int len = nums.size();
        if(len==0)return 0;
        int i=0,j=0;
        for(;i<len;){
            if(nums[i]!=val){nums[j++]=nums[i++];}
            else i++;
        }
        return j;
    }
};

