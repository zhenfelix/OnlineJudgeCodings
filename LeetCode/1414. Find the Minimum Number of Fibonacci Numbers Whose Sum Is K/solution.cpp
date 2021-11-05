const int maxn = 45;
int fib[maxn];
bool initialized = false;

class Solution {
public:
    void init(){
        fib[0] = fib[1] = 1;
        for (int j = 2; j < maxn; j++){
            fib[j] = fib[j-1] + fib[j-2];
            // cout << fib[j] << " ";
        }
        // cout << fib[maxn-1] << endl;
    }
    int findMinFibonacciNumbers(int k) {
        if (!initialized)
            init();
        int cnt = 0;
        for (int j = maxn-1; j >= 0 && k; j--){
            if (fib[j] <= k){
                cnt++;
                k -= fib[j];
            }
        }
        return cnt;
    }
};