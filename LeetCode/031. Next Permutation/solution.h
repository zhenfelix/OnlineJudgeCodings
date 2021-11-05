class Solution {
public:
    void reverse(vector<int> &nums, int a, int b){
        for(int i=0;i+a<=(a+b)/2;i++)swap(nums[i+a],nums[b-i]);
        return;
    }
    void nextPermutation(vector<int>& nums) {
        int n=nums.size();
        if(n==0)return;
        int i=n-2;
        for(;i>=0;i--)if(nums[i]<nums[i+1])break;
        if(i<0)reverse(nums,0,n-1);
        else for(int j=n-1;j>i;j--)if(nums[j]>nums[i]){
            swap(nums[j],nums[i]);
            reverse(nums,i+1,n-1);
            break;
        }
        return ;
    }
};

// static const auto io_sync_off = []()
// {
//     std::ios::sync_with_stdio(false);
//     std::cin.tie(nullptr);
//     std::cout.tie(nullptr);
//     return nullptr;
// }();



class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        int i = n-2;
        for (; i >= 0 && nums[i] >= nums[i+1]; i--){}
        if (i < 0){
            for (int i = 0, j = n-1; i < j; i++, j--)
                swap(nums[i],nums[j]);
            return;
        }
        // cout << i << endl;
        int j = i+1;
        for (; j < n && nums[j] > nums[i]; j++){}
        j--;
        swap(nums[i],nums[j]);
        i++;
        for (int j = n-1; i < j; i++, j--)
            swap(nums[i],nums[j]);
        return;
    }
};