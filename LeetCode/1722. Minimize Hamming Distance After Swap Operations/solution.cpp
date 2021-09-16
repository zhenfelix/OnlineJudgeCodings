class Solution {
public:
    int getf(vector<int>& f, int x) {
        if (f[x] == x) return x;
        int nf = getf(f, f[x]);
        f[x] = nf;
        return nf;
    }
    
    void add(vector<int>& f, int x, int y) {
        int fx = getf(f, x);
        int fy = getf(f, y);
        f[fx] = fy;
    }
    
    int minimumHammingDistance(vector<int>& source, vector<int>& target, vector<vector<int>>& allowedSwaps) {
        int n = source.size();
        vector<int> f(n);
        for (int i = 0; i < n; i++) {
            f[i] = i;
        }
        for (const auto& e: allowedSwaps) {
            add(f, e[0], e[1]);
        }
        
        unordered_map<int, unordered_multiset<int>> s, t; // 为每个联通分支维护位置的集合
        for (int i = 0; i < n; i++) {
            int fa = getf(f, i);
            s[fa].insert(source[i]);
            t[fa].insert(target[i]);
        }
        
        int ret = 0;
        for (int i = 0; i < n; i++) {
            if (s.find(i) == s.end()) continue;
            for (int x: s[i]) {
                if (t[i].find(x) == t[i].end()) {
                    ret++;
                } else {
                    // 不能使用 t[i].erase(x)，不然会删掉所有的 x
                    t[i].erase(t[i].find(x));
                }
            }
        }
        return ret;
    }
};


作者：Arsenal-591
链接：https://leetcode-cn.com/problems/minimize-hamming-distance-after-swap-operations/solution/bing-cha-ji-yao-shao-wei-dong-dian-nao-j-feis/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。