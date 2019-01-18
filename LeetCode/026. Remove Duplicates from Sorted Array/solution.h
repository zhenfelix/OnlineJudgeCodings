#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int len = nums.size();
        if(len==0)return 0;
        int i=0,j=0;
        for(;i<len;){
            if(nums[i]!=nums[j]){nums[++j]=nums[i++];}
            else i++;
        }
        j++;
        return j;
    }
};
