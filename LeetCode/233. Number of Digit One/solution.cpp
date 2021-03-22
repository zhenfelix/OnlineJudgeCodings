class Solution {
public:
    int countDigitOne(int n) {
        int cnt = 0;
        long long base = 1;
        while(base <= n){
            int prefix = n/base;
            int suffix = n%base;
            if (prefix%10 > 1){
                cnt += (prefix/10+1)*base;
            }
            else if(prefix%10 == 1){
                cnt += prefix/10*base;
                cnt += suffix+1;
            }
            else{
                cnt += prefix/10*base;
            }
            // cout << base << " " << cnt << endl;
            base *= 10;
        }
        return cnt;
    }
};