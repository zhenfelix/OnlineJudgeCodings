class Solution {
public:
    int totalSteps(vector<int>& nums) {
        list<int> lst(nums.begin(), nums.end());
        vector<list<int>::iterator> to_del;
        for (auto p = lst.begin(); next(p) != lst.end(); ++p) {
            if (*p > *next(p))
                to_del.push_back(next(p));
        }
        
        int ans = 0;
        while (!to_del.empty()) {
            ans++;
            vector<list<int>::iterator> check;
            for (auto p : to_del) {
                auto pre = prev(p);
                lst.erase(p);
                if (check.empty() || check.back() != pre)
                    check.push_back(pre);
            }
            to_del.clear();
            for (auto p: check) {
                if (next(p) != lst.end() && *p > *next(p))
                    to_del.push_back(next(p));
            }
        }
        
        return ans;
    }
};


// 作者：吴自华
// 链接：https://leetcode.cn/circle/discuss/E0MOm0/view/H6Uk7Z/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution {
public:
    int totalSteps(vector<int>& nums) {
        // 单调栈
        // 1. 每个元素一定时被左侧第一个更大的元素消除的
        // 2. 设 x 消除 y，也就是 [x] .... [y]，那么
        //    中间的 .... 一定先被消除，再 +1 次消除（x 消除 y）
        // 3. 那么，x 被消除所需轮数就是 [....] 中的最大消除轮数 + 1
        int res = 0, f[nums.size()];
        stack<int> st;
        for(int i = 0; i < nums.size(); ++i) {
            int cur = 0;
            while(st.size() && nums[st.top()] <= nums[i]) {
                cur = max(cur, f[st.top()]);
                st.pop();
            }
            if(st.size()) {
                res = max(res, cur + 1);
                f[i] = cur + 1;
            }
            st.push(i);
        }
        return res;
    }
};


// 作者：newhar
// 链接：https://leetcode.cn/problems/steps-to-make-array-non-decreasing/solution/by-newhar-6k75/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution {
public:
    int totalSteps(vector<int>& nums) {
        // 尾部加入一个很大的数方便后续编码
        nums.push_back(1e9 + 8);
        int n = nums.size(), ne[n], rem[n];
        for(int i = 0; i < n; ++i) ne[i] = i+1, rem[i] = 1;
        
        vector<int> v;
        for(int i = n-2; i >= 0; --i) {
            if(nums[i] > nums[i+1]) v.push_back(i);
        }
        
        for(int op = 0;; ++op) {
            vector<int> v2;
            for(int i : v) {
                if(rem[i] && nums[i] > nums[ne[i]]) {
                    rem[ne[i]] = 0;
                    ne[i] = ne[ne[i]];
                    v2.push_back(i);
                }
            }
            if(v2.size()) {
                v.swap(v2);
            } else {
                return op;
            }
        }
        
        // 不可达
        return -1;
    }
};


// 作者：newhar
// 链接：https://leetcode.cn/problems/steps-to-make-array-non-decreasing/solution/by-newhar-6k75/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。