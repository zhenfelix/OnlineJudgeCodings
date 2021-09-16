class Solution {
public:
    int getMaximumGenerated(int n) {
        if (n <= 1)
            return n;
        vector<int> arr(n+1);
        arr[0] = 0, arr[1] = 1;
        int res = 1;
        for (int i = 2; i <= n; i++){
            if (i&1){
                arr[i] = arr[i/2]+arr[i/2+1];
            }
            else
                arr[i] = arr[i/2];
            res = max(res, arr[i]);
        }
        return res;
    }
};