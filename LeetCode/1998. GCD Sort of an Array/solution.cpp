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

class Solution {
public:
    vector<int> spf; // spf[x] is the smallest prime factor of number x, where x >= 2
    bool gcdSort(vector<int>& nums) {
        int maxNum = *max_element(nums.begin(), nums.end());
        sieve(maxNum);

        UnionFind uf(maxNum+1);
        for (int x : nums)
            for (int f : getFactors(x))
                uf.Union(f, x);

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

    vector<int> getFactors(int n) { // O(logN)
        vector<int> factors;
        while (n > 1) {
            factors.push_back(spf[n]);
            n /= spf[n];
        }
        return factors;
    }
};