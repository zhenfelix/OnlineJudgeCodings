class Solution {
public:
    long long test(int a, int index, int n){
        long long res = 0;
        int b = max(0, a-index);
        res += (long long) (a+b)*(a-b+1)/2;
        b = max(0, a-(n-1-index));
        res += (long long) (a+b)*(a-b+1)/2;
        return res-a;
    }

    int maxValue(int n, int index, int maxSum) {
        maxSum -= n;
        int left = 0, right = maxSum;
        while (left <= right){
            int mid = (left+right)/2;
            long long sums = test(mid, index, n);
            if (sums > maxSum){
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }
        return right + 1;
    }
};