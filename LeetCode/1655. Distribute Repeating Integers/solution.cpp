class Solution {
public:
    bool canDistribute(vector<int>& nums, vector<int>& quantity) {
        int n = quantity.size();
        unordered_map<int,int> cc;
        for (auto x : nums)
            cc[x]++;
        vector<int> arr;
        for (auto [k,v] : cc)
            arr.push_back(v);
        int m = arr.size();
        vector<bool> dp(1<<n,false);
        vector<int> sums(1<<n,0);
        // sort(arr.begin(), arr.end(), greater<>());
        // sort(quantity.begin(), quantity.end());
        for (int s = 0; s < (1<<n); s++){
            for (int j = 0; j < n; j++)
                if ((s>>j)&1)
                    sums[s] += quantity[j];
        }
        dp[0] = true;
        for (int i = 0; i < m; i++){
            
            for (int mask = (1<<n)-1; mask; mask--){
                for (int s = mask;; s = (s-1)&mask){
                    if (dp[s] && (sums[mask^s] <= arr[i])){
                        dp[mask] = true;
                        break;
                    }
                    if (s == 0)
                        break;
                }
            }
        }
        return dp.back();
    }
};

// class Solution {
// public:
//     int n;
//     int memo[50][1<<10];
//     bool canDistribute(vector<int>& nums, vector<int>& quantity) {
//         vector<int> cnt(1001);
//         n=quantity.size();
//         for(int i:nums) cnt[i]++;
//         vector<int> freqs;
//         for(int i:cnt){
//             if(i>0) freqs.push_back(i);
//         }
        
//         return dfs(freqs,0,0,quantity);
//     }
    
//     bool dfs(vector<int>& freqs, int idx, int state, vector<int>& quantity){
//         if(state==( (1<<n)-1 ) ) return true;
//         if(idx==freqs.size()) return false;
        
//         if(memo[idx][state]!=0) return false;
//         if(dfs(freqs,idx+1,state,quantity)) return true;
       
//         for(int i=0;i<(1<<n) ;i++){
//             if(i==state) continue;
//             if( (state&i) !=state) continue;
//             int sum=0;
            
//             for(int j=0;j<n;j++){
//                 if( (state&(1<<j)) ==0 && (i&(1<<j))!=0){
//                     sum+=quantity[j];
//                 }
//             }
//             if(sum<=freqs[idx]){
//                 if(dfs(freqs,idx+1,i,quantity)) return true;
//             }
//         }
//         memo[idx][state]=1;
//         return false;
//     }
// };

class Solution {
public:
    bool canDistribute(vector<int>& nums, vector<int>& quantity) {
        unordered_map<int, int> cache;
        for (int x: nums) {
            cache[x]++;
        }
        vector<int> cnt;
        for (auto& kv: cache) {
            cnt.push_back(kv.second);
        }
        
        int n = cnt.size(), m = quantity.size();
        vector<int> sum(1 << m, 0);
        for (int i = 1; i < (1 << m); i++) {
            for (int j = 0; j < m; j++) {
                if ((i & (1 << j)) != 0) {
                    int left = i - (1 << j);
                    sum[i] = sum[left] + quantity[j];
                    break;
                }
            }
        }
        
        vector<vector<bool>> dp(n, vector<bool>(1 << m, false));
        for (int i = 0; i < n; i++) {
            dp[i][0] = true;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < (1 << m); j++) {
                if (i > 0 && dp[i-1][j]) {
                    dp[i][j] = true;
                    continue;
                }
                for (int s = j; s != 0; s = ((s - 1) & j)) { // 子集枚举，详见 https://oi-wiki.org/math/bit/#_14
                    int prev = j - s; // 前 i-1 个元素需要满足子集 prev = j-s
                    bool last = (i == 0) ? (prev == 0): dp[i-1][prev]; // cnt[0..i-1] 能否满足子集 prev
                    bool need = sum[s] <= cnt[i]; // cnt[i] 能否满足子集 s
                    if (last && need) {
                        dp[i][j] = true;
                        break;
                    }
                }
            }
        }
        return dp[n-1][(1<<m)-1];
    }
};


// 作者：Arsenal-591
// 链接：https://leetcode-cn.com/problems/distribute-repeating-integers/solution/zi-ji-mei-ju-jing-dian-tao-lu-zhuang-ya-dp-by-arse/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。