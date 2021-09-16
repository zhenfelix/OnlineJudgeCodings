// using ll = long long;

// class Solution {
// public:
//     void inline dfs(set<ll> &s, vector<int> &nums, int limit, int idx, int cur){
//         if (idx == limit){
//             s.insert(cur);
//             return;
//         }
//         dfs(s,nums,limit,idx+1,cur);
//         dfs(s,nums,limit,idx+1,cur+nums[idx]);
//         return;
//     }
//     int minAbsDifference(vector<int>& nums, int goal) {
//         int n = nums.size();
//         int m = n/2;
//         set<ll> s1, s2;
//         dfs(s1,nums,m,0,0);
//         dfs(s2,nums,n,m,0);
//         ll res = LONG_MAX;
//         for (auto x : s1){
//             res = min(res, abs(goal-x));
//             auto it = s2.lower_bound(goal-x);
//             if (it != s2.end()){
//                 res = min(res, x+(*it)-goal);
//             }
//             if (it != s2.begin()){
//                 res = min(res, goal-(x+(*(--it))));
//             }
//         }
//         return res;
//     }
// };



class Solution {
public:
    void inline dfs(vector<int> &s, vector<int> &nums, int limit, int idx, int cur){
        if (idx == limit){
            s.push_back(cur);
            return;
        }
        dfs(s,nums,limit,idx+1,cur);
        dfs(s,nums,limit,idx+1,cur+nums[idx]);
        return;
    }
    int minAbsDifference(vector<int>& nums, int goal) {
        int n = nums.size();
        if (n == 1)
            return min(abs(goal),abs(goal-nums[0]));
        int m = n/2;
        vector<int> s1, s2;
        dfs(s1,nums,m,0,0);
        dfs(s2,nums,n,m,0);
        sort(s1.begin(), s1.end());
        sort(s2.begin(), s2.end());
        int res = INT_MAX;
        int right = s2.size()-1;
        for (int left = 0; left < s1.size() && right >= 0; left++){
            while (right >= 0 && s1[left]+s2[right] >= goal)
                right--;
            if (right >= 0)
                res = min(res, goal-(s1[left]+s2[right]));
            if (right+1 < s2.size())
                res = min(res,s1[left]+s2[right+1]-goal);
        }
        return res;
    }
};


const int maxn = 21;

class Solution {
public:
    void inline gen(vector<int> &s, vector<int> &nums, unordered_map<int,int> &mp){
        int sz = nums.size();
        s[0] = 0;
        for (int i = 1; i < (1<<sz); i++){
            s[i] = s[i-(i&(-i))] + nums[mp[i&(-i)]];
        }
        return;
    }
    int minAbsDifference(vector<int>& nums, int goal) {
        int n = nums.size(), lm, rm;
        if (n == 1)
            return min(abs(goal),abs(goal-nums[0]));
        lm = n/2, rm = n-n/2;
        vector<int> s1(1<<lm), s2(1<<rm);
        unordered_map<int,int> mp;
        for (int i = 0; i < maxn; i++)
            mp[1<<i] = i;
        vector<int> nums1(nums.begin(), nums.begin()+lm);
        vector<int> nums2(nums.begin()+lm, nums.end());
        gen(s1, nums1, mp);
        gen(s2, nums2, mp);
        sort(s1.begin(), s1.end());
        sort(s2.begin(), s2.end());
        int res = INT_MAX;
        int right = s2.size()-1;
        for (int left = 0; left < s1.size() && right >= 0; left++){
            while (right >= 0 && s1[left]+s2[right] >= goal)
                right--;
            if (right >= 0)
                res = min(res, goal-(s1[left]+s2[right]));
            if (right+1 < s2.size())
                res = min(res,s1[left]+s2[right+1]-goal);
        }
        return res;
    }
};





class Solution {
public:
    void gen(vector<int>& sum, vector<int>& num){
    sum.push_back(0);
    for(int x : num){
        vector<int> nsum;
        int n = sum.size();
        for(int i = 0, j = 0; i < n or j < n;)
            if(i == n) nsum.push_back(sum[j ++] + x);
            else if(j == n) nsum.push_back(sum[i ++]);
            else if(sum[i] < sum[j] + x) nsum.push_back(sum[i ++]);
            else nsum.push_back(sum[j ++] + x);
        swap(nsum, sum);
    }
}


// 作者：Heltion
// 链接：https://leetcode-cn.com/problems/closest-subsequence-sum/solution/o2n2de-zuo-fa-by-heltion-0yn7/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    int minAbsDifference(vector<int>& nums, int goal) {
        int n = nums.size(), lm, rm;
        if (n == 1)
            return min(abs(goal),abs(goal-nums[0]));
        lm = n/2, rm = n-n/2;
        vector<int> s1, s2;
        vector<int> nums1(nums.begin(), nums.begin()+lm);
        vector<int> nums2(nums.begin()+lm, nums.end());
        gen(s1, nums1);
        gen(s2, nums2);
        // sort(s1.begin(), s1.end());
        // sort(s2.begin(), s2.end());
        int res = INT_MAX;
        int right = s2.size()-1;
        for (int left = 0; left < s1.size() && right >= 0; left++){
            while (right >= 0 && s1[left]+s2[right] >= goal)
                right--;
            if (right >= 0)
                res = min(res, goal-(s1[left]+s2[right]));
            if (right+1 < s2.size())
                res = min(res,s1[left]+s2[right+1]-goal);
        }
        return res;
    }
};
