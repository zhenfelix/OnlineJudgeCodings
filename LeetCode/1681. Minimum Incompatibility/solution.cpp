const int inf = 0x3f3f3f3f;

class Solution {
public:
    int minimumIncompatibility(vector<int>& nums, int k) {
        int n = nums.size();
        int cnt = n/k;
        vector<int> cost(1<<n,-1);
        for (int s = 0; s < (1<<n); s++)
            if (__builtin_popcount(s) == cnt){
                vector<int> freq(n+1,0);
                bool flag = true;
                int mi = n+1, mx = 0;
                for (int j = 0; j < n; j++)
                    if ((s>>j)&1){
                        if ((++freq[nums[j]]) > 1){
                            flag = false;
                            break;
                        }
                        mi = min(mi,nums[j]);
                        mx = max(mx,nums[j]);
                    }
                if (flag)
                    cost[s] = mx-mi;
            }

        vector<int> dp(1<<n,inf);
        dp[0] = 0;
        for (int mask = 1; mask < (1<<n); mask++){
            if (__builtin_popcount(mask)%cnt == 0){
                for (int s = mask; s; s = (s-1)&mask){
                    if (cost[s] != -1 && dp[s^mask] < inf){
                        dp[mask] = min(dp[mask], cost[s]+dp[s^mask]);
                    }
                }
            }
        }
        return dp.back() == inf ? -1 : dp.back();
    }
};










class Solution {
public:
    int minimumIncompatibility(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> value(1 << n, -1);
        vector<int> freq(n + 1);
        for (int sub = 0; sub < (1 << n); ++sub) {
            // 判断 sub 是否有 n/k 个 1
            if (__builtin_popcount(sub) == n / k) {
                // 使用数组进行计数
                for (int j = 0; j < n; ++j) {
                    if (sub & (1 << j)) {
                        ++freq[nums[j]];
                    }
                }
                // 任意一个数不能出现超过 1 次
                bool flag = true;
                for (int j = 1; j <= n; ++j) {
                    if (freq[j] > 1) {
                        flag = false;
                        break;
                    }
                }
                // 如果满足要求，那么计算 sub 的不兼容性
                if (flag) {
                    int lb = INT_MAX, rb = INT_MIN;
                    for (int j = 1; j <= n; ++j) {
                        if (freq[j] > 0) {
                            lb = min(lb, j);
                            rb = max(rb, j);
                        }
                    }
                    value[sub] = rb - lb;
                }
                // 由于我们使用数组进行计数，因此要将数组恢复原状
                for (int j = 0; j < n; ++j) {
                    if (sub & (1 << j)) {
                        --freq[nums[j]];
                    }
                }
            }
        }
        
        vector<int> f(1 << n, -1);
        f[0] = 0;
        for (int mask = 1; mask < (1 << n); ++mask) {
            // 判断 mask 是否有 n/k 倍数个 1
            if (__builtin_popcount(mask) % (n / k) == 0) {
                // 枚举子集
                for (int sub = mask; sub; sub = (sub - 1) & mask) {
                    if (value[sub] != -1 && f[mask ^ sub] != -1) {
                        if (f[mask] == -1) {
                            f[mask] = f[mask ^ sub] + value[sub];
                        }
                        else {
                            f[mask] = min(f[mask], f[mask ^ sub] + value[sub]);
                        }
                    }
                }
            }
        }
            
        return f[(1 << n) - 1];
    }
};


作者：zerotrac2
链接：https://leetcode-cn.com/problems/minimum-incompatibility/solution/zui-xiao-bu-jian-rong-xing-by-zerotrac2-rwje/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。