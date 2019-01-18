single loop solution
```c++
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
          int non_zero_index = 0;
          for(int i = 0 ; i < nums.size(); i++) {
              if ( nums[i] != 0) {
                  int temp = nums[non_zero_index];
                  nums[non_zero_index++] = nums[i];
                  nums[i] = temp;
              }
          }
        }
};
```
