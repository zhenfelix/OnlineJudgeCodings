class Solution {
public:
    long long coutPairs(vector<int>& nums, int k) {
        unordered_map<int, int> mp;
        for (int& nu: nums) {
            mp[gcd(nu, k)]++;
        }
        long long res = 0;
        for (auto& [a, c1]: mp) {
            for (auto & [b, c2]: mp) {
                if (a <= b && a*(long) b %k == 0) {
                    res += a < b?(long)c1*c2:(long)c1*(c1-1)/2;
                }
            }
        }
        return res;    
    }
};

class Solution {
public:
    long long coutPairs(vector<int>& nums, int k) {
        int mx = k;
        for (int x : nums) mx = max(mx, x);

        // 统计每个数的倍数出现的次数
        vector<int> cnt(mx + 1), cnt2(mx + 1);
        for (int x : nums) cnt[x]++;
        // 为什么这个算法是 O(nlnn) 的？因为这个算法的循环次数是 n(1 + 1/2 + 1/3 + ...)，由调和级数可知括号内趋向 lnn
        for (int i = 1; i*i <= k; i++){
            if (k%i) continue;
            for (int j = i; j <= mx; j += i) cnt2[i] += cnt[j];
            int ii = k/i;
            if (ii == i) continue;
            for (int j = ii; j <= mx; j += ii) cnt2[ii] += cnt[j];
        }

        long long ans = 0;
        // 对于每个数统计与它形成好二元组的数有几个
        for (int x : nums) ans += cnt2[k / __gcd(k, x)];
        // 排除自己和自己形成好二元组的情况
        for (int x : nums) if (1LL * x * x % k == 0) ans--;
        return ans / 2;
    }
};


// 作者：tsreaper
// 链接：https://leetcode-cn.com/problems/count-array-pairs-divisible-by-k/solution/shu-xue-ji-shu-by-tsreaper-7ok1/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。




class Solution {
public:
    long long coutPairs(vector<int>& nums, int k) {
        long long ans = 0;
        int mx = k;
        for (int x : nums) mx = max(mx, x);

        vector<int> cnt(mx + 1);
        for (int x : nums) {
            int g = k/__gcd(x, k);
            ans += cnt[g];
            for (int q = 1; q*q <= k; q++){
                if (k%q == 0){
                    if (x%q == 0) cnt[q]++;
                    int p = k/q;
                    if (p == q) continue;
                    if (x%p == 0) cnt[p]++;
                }
            }
        }
      
        return ans;
    }
};


const int mx = 100001;
vector<int> divisors[mx];

int init = []() { // 预处理每个数的所有因子，时间复杂度 O(MlogM)，M=1e5
    for (int i = 1; i < mx; ++i)
        for (int j = i; j < mx; j += i)
            divisors[j].push_back(i);
    return 0;
}();

class Solution {
public:
    long long coutPairs(vector<int> &nums, int k) {
        long long ans = 0;
        unordered_map<int, int> cnt;
        for (int v : nums) {
            ans += cnt[k / gcd(v, k)];
            for (int d : divisors[v])
                ++cnt[d];
        }
        return ans;
    }
};


作者：endlesscheng
链接：https://leetcode-cn.com/problems/count-array-pairs-divisible-by-k/solution/tong-ji-yin-zi-chu-xian-ci-shu-by-endles-t5k8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution {
public:
    long long coutPairs(vector<int> &nums, int k) {
        vector<int> divisors; 
        for (int d = 1; d * d <= k; ++d) { // 预处理 k 的所有因子
            if (k % d == 0) {
                divisors.push_back(d);
                if (d * d < k) divisors.push_back(k / d);
            }
        }
        long long ans = 0;
        unordered_map<int, int> cnt;
        for (int v : nums) {
            ans += cnt[k / gcd(v, k)];
            for (int d : divisors)
                if (v % d == 0) ++cnt[d];
        }
        return ans;
    }
};


作者：endlesscheng
链接：https://leetcode-cn.com/problems/count-array-pairs-divisible-by-k/solution/tong-ji-yin-zi-chu-xian-ci-shu-by-endles-t5k8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。