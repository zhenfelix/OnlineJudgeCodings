class Solution {
public:
    int minimumOneBitOperations(int n) {
        if (n == 0)
            return 0;
        int i = 0;
        for (;n>=(1<<i);i++){}
        // cout << n << " " << i << endl;
        return (1<<i)-1-minimumOneBitOperations(n-(1<<(i-1)));
    }
};