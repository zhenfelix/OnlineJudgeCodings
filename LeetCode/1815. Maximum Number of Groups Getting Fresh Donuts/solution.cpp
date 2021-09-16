
// class Solution {
// public:
// map<vector<int>, int> dp;
// int dfs(vector<int>& cnt, int left) {
//     auto it = dp.find(cnt);
//     if (it != end(dp))
//         return it->second;
//     int res = 0;
//     for (auto j = 0; j < cnt.size(); ++j) {
//         if (cnt[j] == 0 || (cnt[left] && j != left))
//             continue;
//         cnt[j] -= 1;
//         res = max(res, (left == 0) + dfs(cnt, (cnt.size() + left - j) % cnt.size()));
//         cnt[j] += 1;
//     }
//     return dp[cnt] = res;
// }
// int maxHappyGroups(int batchSize, vector<int>& groups) {
//     vector<int> cnt(batchSize);
//     for (auto group : groups)
//         ++cnt[group % batchSize];
//     return dfs(cnt, 0);
// }
// };

int freq0[9], freq[9], w[9], f[300000];
class Solution {
public:
    int maxHappyGroups(int b, vector<int>& groups) {
        for(int i = 0; i < b; ++i) freq0[i] = 0;
        for(int i : groups) freq0[i % b]++;
        int msum = 1;
        for(int i = 1; i < b; ++i) msum *= (freq0[i] + 1);
        w[1] = 1;
        for(int i = 2; i < b; ++i) w[i] = w[i-1] * (freq0[i-1] + 1);
        for(int fmask = 0; fmask < msum; ++fmask) f[fmask] = 0;
        for(int fmask = 1; fmask < msum; ++fmask) {
            int last = 0;
            for(int i = 1; i < b; ++i) {
                freq[i] = (fmask / w[i]) % (freq0[i] + 1);
                last = (last + (freq0[i] - freq[i]) * i) % b;
            }
            for(int c = 1; c < b; ++c) {
                if(freq[c]) f[fmask] = max(f[fmask], f[fmask - w[c]] + (last == 0));
            }
        }
        return f[msum-1] + freq0[0];
    }
};


// 作者：newhar
// 链接：https://leetcode-cn.com/problems/maximum-number-of-groups-getting-fresh-donuts/solution/cong-zui-zhi-jie-de-fang-fa-kai-shi-yi-b-x729/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution {
public:
    int maxHappyGroups(int batchSize, vector<int>& groups) {
        vector<int> cnt(batchSize,0);
        for (auto g : groups)
            cnt[g%batchSize]++;
        int tot = 1;
        for (int i = 1; i < batchSize; i++){
            tot *= (cnt[i]+1);
            // cout << i << " " << cnt[i] << endl;
        }
        // cout << tot << endl;
        vector<vector<int>> dp(tot,vector<int>(batchSize,0));
        for (int i = 1; i < tot; i++){
            for (int j = 0; j < batchSize; j++){
                int cur = i, base = 1;
                for (int k = 1; k < batchSize; k++){
                    if (base > i)
                        break;
                    if (cur%(cnt[k]+1))
                        dp[i][j] = max(dp[i][j], dp[i-base][(j-k+batchSize)%batchSize]);
                    base *= (cnt[k]+1);
                    cur /= (cnt[k]+1);
                }
                if (j == 0)
                    dp[i][j]++;
                // cout << i << " " << j << " " << dp[i][j] << endl;
            }
        }
        return cnt[0]+dp[tot-1][0];
    }
};


class Solution {
public:
    int maxHappyGroups(int batchSize, vector<int>& groups) {
        vector<int> cnt(batchSize,0);
        for (auto g : groups)
            cnt[g%batchSize]++;
        int tot = 1, sums = 0;
        for (int i = 1; i < batchSize; i++){
            tot *= (cnt[i]+1);
            sums += cnt[i]*i;
        }
        vector<int> dp(tot,0);
        for (int i = 1; i < tot; i++){
            int cur = i, base = 1, cursums = 0;
            for (int k = 1; k < batchSize; k++){
                if (base > i)
                    break;
                if (cur%(cnt[k]+1)){
                    cursums += (cur%(cnt[k]+1))*k;
                    dp[i] = max(dp[i], dp[i-base]);
                }
                base *= (cnt[k]+1);
                cur /= (cnt[k]+1);
            }
            if ((sums-cursums)%batchSize == 0)
                dp[i]++;
        }
        return cnt[0]+dp[tot-1];
    }
};