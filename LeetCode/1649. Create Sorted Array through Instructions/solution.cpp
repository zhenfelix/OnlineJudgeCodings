using ll = long long;

const int MOD = 1e9+7;
const int maxn = 1e5+10;
int tree[maxn];

class Solution {
public:
    void insert(int x){
        while (x <= maxn){
            tree[x]++;
            x += (x&(-x));
        }
    }
    int query(int x){
        int sums = 0;
        while (x){
            sums += tree[x];
            x -= (x&(-x));
        }
        return sums;
    }
    int createSortedArray(vector<int>& instructions) {
        memset(tree, 0, maxn*sizeof(int));
        ll res = 0;
        int cnt = 0;
        for (auto x : instructions){
            res += min(query(x-1), cnt-query(x));
            res %= MOD;
            cnt++;
            insert(x);
        }
        return res;

    }
};