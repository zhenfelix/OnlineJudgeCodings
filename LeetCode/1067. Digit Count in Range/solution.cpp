using ll = long long;

const int maxn = 12;
ll pow10[maxn];
int dp[maxn][2][2][2];
int cnt[maxn][2][2][2];


class Solution {
public:
    int digitsCount(int d, int low, int high) {
        memset(pow10, 0, maxn*sizeof(int));
        memset(dp, 0, maxn*8*sizeof(int));
        memset(cnt, 0, maxn*8*sizeof(int));
        pow10[1] = 1;
        for (int i = 2; i < maxn; i++)
            pow10[i] = 10*pow10[i-1];
        int n = 1;
        while (pow10[n] <= high)
            n++;
        cnt[0][0][0][0] = cnt[0][0][1][0] = cnt[0][1][0][0] = cnt[0][1][1][0] = 1;
        cnt[0][0][0][1] = cnt[0][0][1][1] = cnt[0][1][0][1] = cnt[0][1][1][1] = 1;
        for (int i = 1; i < n; i++){
            for (int lo = 0; lo <= 1; lo++){
                for (int hi = 0; hi <= 1; hi++){
                    for (int head = 0; head <= 1; head++){
                        int start = lo ? low/pow10[i]%10 : -1, finish = hi ? high/pow10[i]%10 : 10;
                        for (int k = 0; k <= 9; k++){
                            if (k >= start && k <= finish){
                                // if (!(head&&(k==0)) || i = =1)
                                if (!(head&&(k==0))){
                                    dp[i][lo][hi][head] += (k == d)*cnt[i-1][k==start][k==finish][head&(k==0)];
                                }
                                dp[i][lo][hi][head] += dp[i-1][k==start][k==finish][head&(k==0)];
                                cnt[i][lo][hi][head] += cnt[i-1][k==start][k==finish][head&(k==0)];
                            }
                        }
                    }
                }
            }
        }
        return dp[n-1][1][1][1];

    }
};


class Solution {
    public int digitsCount(int d, int low, int high) {
        return count(high, d) - count(low - 1, d);
    }
    
    /* 计算数字 d 在 1-n 中出现的次数。 */
    public int count(int n, int d) {
        int cnt = 0, k;
        for (int i = 1;(k = n / i) != 0;i *= 10) {
            // 高位的数字。
            int high = k / 10;
            if (d == 0) {
                if (high != 0) {
                    high--;
                } else {
                    break;
                }
            }
            cnt += high * i;
            // 当前位的数字。
            int cur = k % 10;
            if (cur > d) {
                cnt += i;
            } else if (cur == d) {
                // n - k * i 为低位的数字。
                cnt += n - k * i + 1;
            }
        }
        return cnt;
    }
    
}


作者：Jiachen_Zhang
链接：https://leetcode-cn.com/problems/digit-count-in-range/solution/shu-xue-gui-na-fa-zhao-gui-lu-chun-shu-xue-by-jiac/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。