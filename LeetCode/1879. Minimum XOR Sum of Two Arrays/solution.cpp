class Solution {
public:
    int minimumXORSum(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        vector<int> f(1 << n, INT_MAX);
        f[0] = 0;
        for (int mask = 1; mask < (1 << n); ++mask) {
            for (int i = 0; i < n; ++i) {
                if (mask & (1 << i)) {
                    f[mask] = min(f[mask], f[mask ^ (1 << i)] + (nums1[__builtin_popcount(mask) - 1] ^ nums2[i]));
                }
            }
        }
        return f[(1 << n) - 1];
    }
};


// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/minimum-xor-sum-of-two-arrays/solution/liang-ge-shu-zu-zui-xiao-de-yi-huo-zhi-z-2uye/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



const static int INF = 0x3f3f3f3f;
const static int maxn = 20;
int match[maxn], lval[maxn], rval[maxn], slack[maxn];
int w[maxn][maxn];
bool  lvisi[maxn], rvisi[maxn];
int n;

bool dfs(int now) {
    lvisi[now] = true;
    for (int i = 0; i < n; ++i) if (!rvisi[i]) {
        int t = lval[now] + rval[i] - w[now][i];
        if (t == 0) {
            rvisi[i] = true;
            if (match[i] == -1 || dfs(match[i])) {
                match[i] = now;
                return true;
            }
        }
        else slack[i] = min(slack[i], t);
    }
    return false;
}

int km() {
    memset(match, -1, sizeof(match));
    memset(rval, 0, sizeof(rval));
    for (int i = 0; i < n; ++i) {
        lval[i] = w[i][0];
        for (int j = 1; j < n; ++j)
            lval[i] = max(lval[i], w[i][j]);
    }
    for (int i = 0; i < n; ++i) {
        fill(slack, slack + n, INF);
        while (1) {
            memset(lvisi, 0, sizeof(lvisi));
            memset(rvisi, 0, sizeof(rvisi));
            if (dfs(i)) break;
            else {
                int d = INF;
                for (int j = 0; j < n; ++j) if (!rvisi[j])
                    d = min(d, slack[j]);
                for (int j = 0; j < n; ++j) {
                    if (lvisi[j]) lval[j] -= d;
                    if (rvisi[j]) rval[j] += d;
                    else slack[j] -= d;
                }
            }
        }
    }
    int res = 0;
    for (int i = 0; i < n; ++i) {
        res += w[match[i]][i];
    }
    return res;
}


class Solution {
public:
    int minimumXORSum(vector<int>& nums1, vector<int>& nums2) {
        n = nums1.size();
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                w[i][j] = -1*(nums1[i] ^ nums2[j]);
            }
        }
        return -1*(km());
    }
};


// 作者：RHPRHP
// 链接：https://leetcode-cn.com/problems/minimum-xor-sum-of-two-arrays/solution/quan-zhi-qu-fu-zhuan-hua-wei-er-fen-tu-d-ju01/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。