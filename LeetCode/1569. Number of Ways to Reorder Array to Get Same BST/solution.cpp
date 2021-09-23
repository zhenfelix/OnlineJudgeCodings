// using ll = long long;
// const int MOD = 1e9+7;
// const int maxn = 1005;
// int fac[maxn], ifac[maxn];
// bool initialized = false;

// struct Node
// {
//     int val;
//     Node *left, *right;
//     Node(int v)
//         : val(v), left(nullptr), right(nullptr)
//         {}
// };

// class Solution {
// public:
//     Node* insert(Node *cur, int x){
//         if (cur == nullptr){
//             cur = new Node(x);
//             return cur;
//         }
//         if (x < cur->val)
//             cur->left = insert(cur->left, x);
//         else
//             cur->right = insert(cur->right, x);
//         return cur;
//     }
//     pair<int,int> dfs(Node *cur){
//         if (cur == nullptr)
//             return {1,0};
//         auto [ways_left, cnt_left] = dfs(cur->left);
//         auto [ways_right, cnt_right] = dfs(cur->right);
//         int res = ((ll)ways_left*ways_right)%MOD;
//         res = ((ll)res*fac[cnt_left+cnt_right])%MOD;
//         res = ((ll)res*ifac[cnt_left])%MOD;
//         res = ((ll)res*ifac[cnt_right])%MOD;
//         return {res,cnt_left+cnt_right+1};
//     }
//     int quickmul(int a, int q){
//         int res = 1;
//         while (q){
//             if (q&1)
//                 res = ((ll)res*a)%MOD;
//             a = ((ll)a*a)%MOD;
//             q >>= 1;
//         }
//         return res;
//     }
//     void init(){
//         fac[0] = ifac[0] = 1;
//         for (int i = 1; i < maxn; i++)
//             fac[i] = ((ll)fac[i-1]*i)%MOD;
//         ifac[maxn-1] = quickmul(fac[maxn-1],MOD-2);
//         for (int i = maxn-2; i >= 1; i--)
//             ifac[i] = ((ll)ifac[i+1]*(i+1))%MOD;
//         initialized = true;
//     }
//     int numOfWays(vector<int>& nums) {
//         if (!initialized)
//             init();
//         Node *root = nullptr;
//         for (auto x : nums)
//             root = insert(root, x);
//         auto [ways, cnt] = dfs(root);
//         return ways-1;
//     }
// };


#define MAXN 1005

typedef long long ll;
const ll MOD = 1e9 + 7;

ll fac[MAXN], rev[MAXN];

ll fexp(ll x, ll y) {
    ll ans = 1;
    while (y) {
        if (y & 1)
            ans = ans * x % MOD;
        x = x * x % MOD;
        y >>= 1;
    }
    return ans;
}

ll C(ll n, ll k) {
    return fac[n] * rev[k] % MOD * rev[n - k] % MOD;
}

class Solution {
    ll dfs(vector<int> &nums) {
        if (nums.size() <= 1)
            return 1;
        vector<int> small, large;
        for (int i = 1; i < nums.size(); ++i)
            if (nums[i] > nums[0])
                large.emplace_back(nums[i]);
            else
                small.emplace_back(nums[i]);
        ll n = large.size(), m = small.size();
        ll fn = dfs(large), fm = dfs(small);
        return C(n + m, n) * fn % MOD * fm % MOD;
    }
public:
    int numOfWays(vector<int>& nums) {
        fac[0] = 1, rev[0] = 1;
        for (int i = 1; i <= nums.size(); ++i) {
            fac[i] = fac[i - 1] * i % MOD;
            rev[i] = fexp(fac[i], MOD - 2);
        }
        return (dfs(nums) % MOD - 1 + MOD) % MOD;
    }
};


// 作者：lucifer1004
// 链接：https://leetcode-cn.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/solution/zu-he-di-gui-by-lucifer1004/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。