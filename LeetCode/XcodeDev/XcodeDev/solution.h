#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <algorithm>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <iostream>
#include <deque>

using namespace std;

class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int n=nums.size();
        int idx=-1, high=INT_MAX, i;
        for(i=0;i<n;i++)if(nums[i]<=high){
            idx=i;
            high=nums[idx];
        }
        for(i=0;i<n;i++)if(nums[(idx+i)%n]>nums[(idx+i+1)%n])break;
        if(i==n-1)return false;
        for(i=0;i<n;i++)if(nums[(idx-i+n)%n]>nums[(idx-i-1+n)%n])break;
        if(i==n-1)return false;
        return true;
    }
};
