class Solution {
public:
    int minimumDeviation(vector<int>& nums) {
        int p_max = 1;
        for(int a : nums) p_max = max(p_max, a >> (__builtin_ctz(a)));
        vector<int> upper;
        int min = p_max;
        for(int a : nums){
            if(a & 1) a <<= 1;
            if(a >= p_max){
                a >>= __builtin_clz(p_max) - __builtin_clz(a);
                if(a < p_max) a <<= 1;
                upper.push_back(a);
            }
            min = std::min(min, a);
        }
        sort(upper.begin(), upper.end());
        int ans = upper.back() - min;
        for(int i = upper.size() - 1; upper[i] > p_max; i -= 1){
            min = std::min(min, upper[i] >> 1);
            ans = std::min(ans, upper[i - 1] - min);
        }
        return ans;
    }
};


作者：Heltion
链接：https://leetcode-cn.com/problems/minimize-deviation-in-array/solution/yi-chong-fu-za-du-geng-di-de-zuo-fa-by-heltion-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。




class Solution 
{
public:
    int minimumDeviation(vector<int>& nums) 
    {
        int min_ = INT_MAX;
        priority_queue<int, vector<int>, less<int>> maxHeap;
        for (int & x: nums)
        {
            if (x % 2 == 1)
                x *= 2;
            min_ = min(min_, x);
            maxHeap.push(x);
        }

        int res = INT_MAX;
        while (maxHeap.size())
        {
            int x = maxHeap.top();    maxHeap.pop();
            res = min(res, x - min_);
            if (x % 2 == 1)
                break;
            x /= 2;
            min_ = min(min_, x);
            maxHeap.push(x);
        }

        return res;
    }
};


// 作者：Hanxin_Hanxin
// 链接：https://leetcode-cn.com/problems/minimize-deviation-in-array/solution/cpython3-zui-da-dui-mo-ni-by-hanxin_hanx-1ruk/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



