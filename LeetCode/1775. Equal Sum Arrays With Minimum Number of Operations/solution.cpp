class Solution {
public:
    int minOperations(vector<int>& nums1, vector<int>& nums2) {
        int sums1 = 0, sums2 = 0;
        vector<int> cnt1(7,0), cnt2(7,0);
        for (auto x : nums1)
            sums1 += x, cnt1[x]++;
        for (auto x : nums2)
            sums2 += x, cnt2[x]++;
        if (sums1 < sums2)
            swap(sums1,sums2), swap(cnt1,cnt2);
        int res = 0, diff = sums1 - sums2, delta = 5;
        while (diff > 0 && delta){
            if (cnt1[1+delta]){
                diff -= delta;
                cnt1[1+delta]--;
                res++;
            }
            else if (cnt2[6-delta]){
                diff -= delta;
                cnt2[6-delta]--;
                res++;
            }
            else
                delta--;
        }
        return delta <= 0 ? -1 : res;
    }
};



class Solution {
public:
    int minOperations(vector<int>& nums1, vector<int>& nums2) {
        int sum1 = accumulate(nums1.begin(), nums1.end(), 0);
        int sum2 = accumulate(nums2.begin(), nums2.end(), 0);
        if (sum1 == sum2) {
            return 0;
        }
        if (sum1 > sum2) {
            return minOperations(nums2, nums1);
        }

        int diff = sum2 - sum1;
        vector<int> freq(6);
        for (int num: nums1) {
            ++freq[6 - num];
        }
        for (int num: nums2) {
            ++freq[num - 1];
        }

        int ans = 0;
        for (int i = 5; i >= 1 && diff > 0; --i) {
            while (freq[i] && diff > 0) {
                ++ans;
                --freq[i];
                diff -= i;
            }
        }

        return (diff > 0 ? -1 : ans);
    }
};


作者：zerotrac2
链接：https://leetcode-cn.com/problems/equal-sum-arrays-with-minimum-number-of-operations/solution/tong-guo-zui-shao-cao-zuo-ci-shu-shi-shu-o8no/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。