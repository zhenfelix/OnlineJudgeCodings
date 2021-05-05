class Solution {
public:
    int numberOf2sInRange(int n) {
        int cnt = 0;
        long long base = 1;
        while (n >= base)
        {
            long long left = n/(10*base), cur = (n/base)%10, right = n%base;
            
            if (left)
                cnt += left*base;
            if (cur >= 2)
            {
                if (cur > 2)
                    cnt += base;
                else
                    cnt += right+1;
            }
            // cout << base << ' ' << left << ' ' << cur << ' ' << right << ' ' << cnt << endl;
            base *= 10;
        }
        return cnt;
    }
};