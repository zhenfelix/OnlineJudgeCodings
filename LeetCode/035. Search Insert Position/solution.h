#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    int binary_search(int left, int right, vector<int>& nums, int target){
        if(left>right)return left;
        int mid = (left+right)/2;
        if(nums[mid]<target)return binary_search(mid+1, right, nums, target);
        else if(nums[mid]>target)return binary_search(left, mid-1, nums, target);
        else return mid;
    }
    int searchInsert(vector<int>& nums, int target) {
        int len = nums.size();
        if(len==0)return 0;
        return binary_search(0, len-1, nums, target);
    }
};

