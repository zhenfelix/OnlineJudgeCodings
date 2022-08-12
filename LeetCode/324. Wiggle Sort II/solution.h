// O(n) space
class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        vector<int> tmp = nums;
        int n = nums.size(), k = (n + 1) / 2, j = n; 
        sort(tmp.begin(), tmp.end());
        for (int i = 0; i < n; ++i) {
            nums[i] = i & 1 ? tmp[--j] : tmp[--k];
        }
    }
};


// O(1) space, bubble sort, TLE
class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        int n = nums.size();
        #define A(i) nums[(1+2*(i)) % (n|1)]
        for (int i = n-1; i >= 1; i--){
            for (int j = 1; j <= i; j++)
                if (A(j-1) < A(j)) swap(A(j-1), A(j));
        }
        return;
    }
};


class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        int n = nums.size();

        // Find a median.
        auto midptr = nums.begin() + n / 2;
        nth_element(nums.begin(), midptr, nums.end());
        int mid = *midptr;

        // Index-rewiring.
        #define A(i) nums[(1+2*(i)) % (n|1)]

        // 3-way-partition-to-wiggly in O(n) time with O(1) space.
        int i = 0, j = 0, k = n - 1;
        while (j <= k) {
            if (A(j) > mid)
                swap(A(i++), A(j++));
            else if (A(j) < mid)
                swap(A(j), A(k--));
            else
                j++;
        }
    }
};


作者：hexcat
链接：https://leetcode.cn/problems/wiggle-sort-ii/solution/yi-bu-yi-bu-jiang-shi-jian-fu-za-du-cong-onlognjia/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。