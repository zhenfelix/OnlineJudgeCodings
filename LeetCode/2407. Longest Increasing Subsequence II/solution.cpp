const int N = 1e5 + 10;
int a[N], h[N];
int lowbit(int x){ return x & (-x);}
void update(int x){
    int lx = x;
    while(x < N) h[x] = max(h[x], a[lx]), x += lowbit(x);
}
int query(int x, int y){
    int ans = 0;
    while(y >= x){
        if (y-lowbit(y) <= x) ans = max(a[y], ans), y --;
        
        for(; y - lowbit(y) > x; y -= lowbit(y)) ans = max(h[y], ans);
    }
    return ans;
} 
class Solution {
public:
    int lengthOfLIS(vector<int>& nums, int k) {
        memset(h, 0, sizeof h), memset(a, 0, sizeof a);
        for(auto& v : nums) a[v] = max(a[v], query(max(1, v - k), v - 1) + 1), update(v);
        return query(1, N - 1);
    }
};


// 作者：crazycoding-feng
// 链接：https://leetcode.cn/problems/longest-increasing-subsequence-ii/solution/shu-zhuang-shu-zu-by-crazycoding-feng-tzil/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution {
public:
    int lengthOfLIS(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> dp(n, 1), p(n);
        for (int i = 0; i < n; i += 1) p[i] = i;
        sort(p.begin(), p.end(), [&](int x, int y){
            return nums[x] == nums[y] ? x > y : nums[x] < nums[y];
        });
        function<void(int, int, vector<int>)> DFS = [&](int L, int R, vector<int> p) {
            if (L >= R) return;
            int M = (L + R) >> 1;
            vector<vector<int>> q(2);
            for (int i : p) q[i > M].push_back(i);
            DFS(L, M, q[0]);
            deque<int> dq;
            for (int i : p)
                if (i <= M) {
                    while (not dq.empty() and dp[dq.back()] <= dp[i]) dq.pop_back();
                    dq.push_back(i);
                }
                else {
                    while (not dq.empty() and nums[dq.front()] < nums[i] - k) dq.pop_front();
                    if (not dq.empty()) dp[i] = max(dp[i], dp[dq.front()] + 1);
                }
            DFS(M + 1, R, q[1]);
        };
        DFS(0, n - 1, p);
        return *max_element(dp.begin(), dp.end());
    }
};


// 作者：Heltion
// 链接：https://leetcode.cn/problems/longest-increasing-subsequence-ii/solution/fen-zhi-by-heltion-h31y/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。