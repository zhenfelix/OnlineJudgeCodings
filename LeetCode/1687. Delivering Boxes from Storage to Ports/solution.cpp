// class Solution {
// public:
//     int boxDelivering(vector<vector<int>>& boxes, int portsCount, int maxBoxes, int maxWeight) {
//         int n = boxes.size();
//         vector<int> dp(n+1, INT_MAX);
//         dp[0] = 0;
//         for (int i = 0; i < n; i++){
//             for (int j = i-1, cnt = 2, sums = boxes[i][1], bx = 1; j+1 >= 0 && sums <= maxWeight && bx <= maxBoxes; j--){
//                 dp[i+1] = min(dp[i+1], dp[j+1]+cnt);
//                 if (j >= 0){
//                     if (boxes[j][0] != boxes[j+1][0])
//                         cnt++;
//                     sums += boxes[j][1];
//                     bx++;
//                 }
//             }
//         }
//         return dp.back();
//     }
// };


using ll = long long;

class Solution {
public:
    int boxDelivering(vector<vector<int>>& boxes, int portsCount, int maxBoxes, int maxWeight) {
        int n = boxes.size();
        vector<int> dp(n+1, INT_MAX), diff_sums(n,0);
        vector<ll> weight_sums(n+1,0);
        dp[0] = 0; weight_sums[0] = boxes[0][1];
        for (int i = 0; i < n; i++){
            weight_sums[i+1] = weight_sums[i]+boxes[i][1];
            if (i){
                diff_sums[i] = diff_sums[i-1];
                if (boxes[i][0] != boxes[i-1][0])
                    diff_sums[i]++;
            }
                
        }
        vector<int> st;
        for (int i = 0; i < n; i++){
            for (int left = i; left >= 0 && i-left+1 <= maxBoxes && weight_sums[i+1]-weight_sums[left] <= maxWeight; left--){
                dp[i+1] = min(dp[i+1], dp[left]-diff_sums[left]+diff_sums[i]+2);
            }
        }
        return dp.back();
    }
};







using ll = long long;

class Solution
{
public:
    int boxDelivering(vector<vector<int>> &boxes, int portsCount, int maxBoxes, int maxWeight)
    {
        int n = boxes.size();
        vector<int> dp(n + 1, INT_MAX), diff_sums(n, 0);
        vector<ll> weight_sums(n + 1, 0);
        dp[0] = 0;
        weight_sums[0] = boxes[0][1];
        for (int i = 0; i < n; i++)
        {
            weight_sums[i + 1] = weight_sums[i] + boxes[i][1];
            if (i)
            {
                diff_sums[i] = diff_sums[i - 1];
                if (boxes[i][0] != boxes[i - 1][0])
                    diff_sums[i]++;
            }
        }
        vector<int> st;
        int left = 0;
        for (int i = 0; i < n; i++)
        {
            while ((left < st.size()) && (dp[st.back()] - diff_sums[st.back()] >= dp[i] - diff_sums[i]))
                st.pop_back();
            st.push_back(i);
            while ((i - st[left] + 1 > maxBoxes) || (weight_sums[i + 1] - weight_sums[st[left]] > maxWeight))
                left++;
            dp[i + 1] = dp[st[left]] - diff_sums[st[left]] + diff_sums[i] + 2;
        }
        return dp.back();
    }
};




class Solution {
public:
    int boxDelivering(vector<vector<int>>& boxes, int _, int bound_num, int bound_w) {
        int n = boxes.size();
        vector<int> p(n + 1), w(n + 1), neg(n + 1);
        vector<long long> W(n + 1);
        for (int i = 1; i <= n; ++i) {
            p[i] = boxes[i - 1][0];
            w[i] = boxes[i - 1][1];
            if (i > 1) {
                neg[i] = neg[i - 1] + (p[i - 1] != p[i]);
            }
            W[i] = W[i - 1] + w[i];
        }
        
        deque<int> opt = {0};
        vector<int> f(n + 1), g(n + 1);
        
        for (int i = 1; i <= n; ++i) {
            while (!opt.empty() && (i - opt.front() > bound_num || W[i] - W[opt.front()] > bound_w)) {
                opt.pop_front();
            }
            
            f[i] = g[opt.front()] + neg[i] + 2;
            
            if (i != n) {
                g[i] = f[i] - neg[i + 1];
                while (!opt.empty() && g[i] <= g[opt.back()]) {
                    opt.pop_back();
                }
                opt.push_back(i);
            }
        }
        
        return f[n];
    }
};


作者：zerotrac2
链接：https://leetcode-cn.com/problems/delivering-boxes-from-storage-to-ports/solution/cong-cang-ku-dao-ma-tou-yun-shu-xiang-zi-dqnq/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。