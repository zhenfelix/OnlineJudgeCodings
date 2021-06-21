class Solution {
public:
    long long calc(int m){
        long sums = 0, cur = 0, rank = 1;
        while (cur+rank < m){
            cur += rank;
            sums += cur;
            rank++;
        }
        long long remains = m - cur;
        sums += (remains+1)*remains/2;
        return sums;
    }

    int minimumBoxes(int n) {
        int lo = 1, hi = n;
        while (lo <= hi){
            int mid = (lo + hi)/2;
            if (calc(mid) >= n){
                hi = mid - 1;
            }
            else{
                lo = mid + 1;
            }
        }
        return lo;
    }
};