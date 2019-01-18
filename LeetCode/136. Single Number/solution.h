#include <vector>
#include <map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        map<int,int> record;
        int ans=0;
        for(int i=0;i<nums.size();i++){
            if(record.count(nums[i]))ans-=nums[i];
            else {
                ans+=nums[i];
                record[nums[i]]=1;
            }
        }
        return ans;
    }
};
