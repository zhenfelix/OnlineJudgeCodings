#define MAXX ((int) 1e5)
bool inited = false;
vector<int> fac[MAXX + 10];

// 全局预处理每个数的质因数
void init() {
    if (inited) return;
    inited = true;

    for (int i = 2; i <= MAXX; i++) if (fac[i].empty()) for (int j = i; j <= MAXX; j += i) fac[j].push_back(i);
}

class Solution {
public:
    bool canTraverseAllPairs(vector<int>& nums) {
        init();

        int n = nums.size();
        int mx = 0;
        for (int x : nums) mx = max(mx, x);

        // 初始化并查集
        int root[n + mx + 1];
        for (int i = 0; i <= n + mx; i++) root[i] = i;

        // 查询并查集的根
        function<int(int)> findroot = [&](int x) {
            if (root[x] != x) root[x] = findroot(root[x]);
            return root[x];
        };

        // 对每个 nums[i]，向它们的质因数连边
        for (int i = 0; i < n; i++) for (int p : fac[nums[i]]) {
            int x = findroot(i), y = findroot(n + p);
            if (x == y) continue;
            root[x] = y;
        }

        // 检查是否所有位置点都在同一连通块内
        unordered_set<int> st;
        for (int i = 0; i < n; i++) st.insert(findroot(i));
        return st.size() == 1;
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/fQ58lb/view/6vKWNF/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。