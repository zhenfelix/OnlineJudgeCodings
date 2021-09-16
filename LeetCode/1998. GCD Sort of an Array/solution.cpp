// Feel free to copy this class for later reuse!
class UnionFind {
    vector<int> parent, size;
public:
    UnionFind(int n) {
        parent.resize(n); size.resize(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i; size[i] = 1;
        }
    }
    void init(int m){
        for (int i = 0; i < m; i++) {
            parent[i] = i; size[i] = 1;
        }
    }
    int find(int x) {
        if (x == parent[x]) return x;
        return parent[x] = find(parent[x]); // Path compression
    }
    bool Union(int u, int v) {
        int pu = find(u), pv = find(v);
        if (pu == pv) return false; // Return False if u and v are already union
        if (size[pu] > size[pv]) { // Union by larger size
            size[pu] += size[pv];
            parent[pv] = pu;
        } else {
            size[pv] += size[pu];
            parent[pu] = pv;
        }
        return true;
    }
};

const int maxn = 1e5+10;
UnionFind uf(maxn+1);
bool initiated = false;
vector<int> spf; // spf[x] is the smallest prime factor of number x, where x >= 2

class Solution {
public:

    void init(){
        sieve(maxn);
        initiated = true;
    }

    void sieve(int n) { // O(Nlog(logN)) ~ O(N)
        // cout << 'a' << endl;
        spf.resize(n+1);
        for (int i = 2; i <= n; ++i)
            spf[i] = i;
        for (int i = 2; i * i <= n; i++) {
            if (spf[i] != i) continue; // skip if `i` is not a prime number
            for (int j = i * i; j <= n; j += i) {
                spf[j] = i;
            }
        }
    }
    
    bool gcdSort(vector<int>& nums) {
        // cout << initiated << " " << spf.size() << " " << maxn << endl;
        if (!initiated)
            init();
        int maxNum = *max_element(nums.begin(), nums.end());
        uf.init(maxNum+1);
        // cout << "a" << endl;

        for (int x : nums)
            for (int f : getFactors(x))
                uf.Union(f, x);
        // cout << "b" << endl;
        vector<int> sortedArr(nums);
        sort(sortedArr.begin(), sortedArr.end());
        
        for (int i = 0; i < nums.size(); ++i) {

            if (sortedArr[i] != nums[i] && uf.find(sortedArr[i]) != uf.find(nums[i])) return false; // can't swap nums[i] to sortedArr[i]
        }
        return true;
    }


    vector<int> getFactors(int n) { // O(logN)
        vector<int> factors;
        while (n > 1) {
            if (factors.empty() || factors.back() != spf[n])
                factors.push_back(spf[n]);
            n /= spf[n];
        }
        // cout << "c" << endl;
        return factors;
    }
};

























// Feel free to copy this class for later reuse!
class UnionFind {
    vector<int> parent, size;
public:
    UnionFind(int n) {
        parent.resize(n); size.resize(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i; size[i] = 1;
        }
    }
    void init(int m){
        for (int i = 0; i < m; i++) {
            parent[i] = i; size[i] = 1;
        }
    }
    int find(int x) {
        if (x == parent[x]) return x;
        return parent[x] = find(parent[x]); // Path compression
    }
    bool Union(int u, int v) {
        int pu = find(u), pv = find(v);
        if (pu == pv) return false; // Return False if u and v are already union
        if (size[pu] > size[pv]) { // Union by larger size
            size[pu] += size[pv];
            parent[pv] = pu;
        } else {
            size[pv] += size[pu];
            parent[pu] = pv;
        }
        return true;
    }
};

const int maxn = 1e5+10;
UnionFind uf(maxn);

class Solution {
public:
    vector<int> spf; // spf[x] is the smallest prime factor of number x, where x >= 2
    bool gcdSort(vector<int>& nums) {
        int maxNum = *max_element(nums.begin(), nums.end());
        sieve(maxNum);

        uf.init(maxNum+1);
        for (int x : nums)
            getFactors(x);

        vector<int> sortedArr(nums);
        sort(sortedArr.begin(), sortedArr.end());
        
        for (int i = 0; i < nums.size(); ++i) {
            int pu = uf.find(sortedArr[i]);
            int pv = uf.find(nums[i]);
            if (pu != pv) return false; // can't swap nums[i] to sortedArr[i]
        }
        return true;
    }

    void sieve(int n) { // O(Nlog(logN)) ~ O(N)
        spf.resize(n+1);
        for (int i = 2; i <= n; ++i)
            spf[i] = i;

        for (int i = 2; i * i <= n; i++) {
            if (spf[i] != i) continue; // skip if `i` is not a prime number
            for (int j = i * i; j <= n; j += i) {
                if (spf[j] == j) { // marking spf[j] if it is not previously marked
                    spf[j] = i;
                }
            }
        }
    }

    void getFactors(int n) { // O(logN) // get rid of frequent vector copying can almost double your speed!
        int f = 1, x = n;
        while (n > 1) {
            if (f != spf[n]){
                f = spf[n];
                uf.Union(f, x);
            }
            n /= spf[n];
        }
        return;
    }
};





















const int maxn = 1e5+10;

// Feel free to copy this class for later reuse!
class UnionFind {
    int parent[maxn], size[maxn];
public:

    void init(int m){
        for (int i = 0; i < m; i++) {
            parent[i] = i; size[i] = 1;
        }
    }
    int find(int x) {
        if (x == parent[x]) return x;
        return parent[x] = find(parent[x]); // Path compression
    }
    bool Union(int u, int v) {
        int pu = find(u), pv = find(v);
        if (pu == pv) return false; // Return False if u and v are already union
        if (size[pu] > size[pv]) { // Union by larger size
            size[pu] += size[pv];
            parent[pv] = pu;
        } else {
            size[pv] += size[pu];
            parent[pu] = pv;
        }
        return true;
    }
};


UnionFind uf;
bool initiated = false;
int spf[maxn]; // spf[x] is the smallest prime factor of number x, where x >= 2

class Solution {
public:

    void init(){
        sieve(maxn-1);
        initiated = true;
    }

    void sieve(int n) { // O(Nlog(logN)) ~ O(N)
        // cout << 'a' << endl;
        for (int i = 2; i <= n; ++i)
            spf[i] = i;
        for (int i = 2; i * i <= n; i++) {
            if (spf[i] != i) continue; // skip if `i` is not a prime number
            for (int j = i * i; j <= n; j += i) {
                spf[j] = i;
            }
        }
    }
    
    bool gcdSort(vector<int>& nums) {
        // cout << initiated << " " << spf.size() << " " << maxn << endl;
        if (!initiated)
            init();
        int maxNum = *max_element(nums.begin(), nums.end());
        uf.init(maxNum+1);
        // cout << "a" << endl;

        for (int x : nums)
            getFactors(x);
                
        // cout << "b" << endl;
        vector<int> sortedArr(nums);
        sort(sortedArr.begin(), sortedArr.end());
        
        for (int i = 0; i < nums.size(); ++i) {

            if (sortedArr[i] != nums[i] && uf.find(sortedArr[i]) != uf.find(nums[i])) return false; // can't swap nums[i] to sortedArr[i]
        }
        return true;
    }


    void getFactors(int n) { // O(logN)
        int f = 1, x = n;
        while (n > 1) {
            if (f != spf[n]){
                f = spf[n];
                uf.Union(f, x);
            }
            n /= spf[n];
        }
        // cout << "c" << endl;
        return;
    }
};









const int N = 3e5 + 10;

class Solution {
private:
    int p[N];
public:
    int find(int x) {
        if (x != p[x])  p[x] = find(p[x]);
        return p[x];
    }
    void merge(int a, int b) {
        int x = find(a), y = find(b);
        if (x == y)     return;
        p[x] = y;
    }
    bool gcdSort(vector<int>& nums) {
        vector<int> nums1 = nums;
        for (int i = 1; i < N; i++) p[i] = i;
        // 分解质因数
        for (auto c:nums) {
            int k = c;
            for (int i = 2; i <= c / i; i++) {
                bool flag = false;
                while (c % i == 0)
                    c /= i, flag = true;
                if (flag)
                    merge(k, i);
            }
            // 合并质因子
            if (c > 1)
               merge(k, c);
        }
        sort(nums1.begin(), nums1.end());
        // 对比原数组
        for (int i = 0; i < nums1.size(); i++) {
            if (nums1[i] == nums[i])    continue;
            if (find(nums1[i]) != find(nums[i]))    return false;
        }
        return true;
    }
};


// 作者：xin-xiang-yuan-fang
// 链接：https://leetcode-cn.com/problems/gcd-sort-of-an-array/solution/bing-cha-ji-fen-jie-zhi-yin-shu-by-xin-x-ylsz/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。