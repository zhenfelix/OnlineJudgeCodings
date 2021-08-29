class Solution {
public:
    int getKthNum(int k) {
        long long sums = 0;
        long long i = 1, base = 1;
        for (;sums < k; i++, base *= 10){
            sums += base*i*9;
            // cout << sums << endl;
        }
        i--;base/=10;
        sums -= i*base*9;
        // cout << sums << ' ' << i << ' ' << base << endl;
        k -= sums;
        int a = (k-1)/i;
        int b = k%i;
        int x = base+a;
        // cout << a << ' ' << b << endl;
        if (b == 0)
            return x%10;
        b = i-b;
        while (b--)
            x /= 10;
        return x%10;

    }
};