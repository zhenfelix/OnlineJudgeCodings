class Solution {
public:
    bool isPowerOfTwo(int n) {
        int TWO=1<<30;
        if(n<1||n>TWO)return false;
        else return TWO%n==0;
    }
};

// class Solution {
// public:
//     bool isPowerOfTwo(int n) {
//         return n > 0 && (n&(n-1)) == 0;
//     }
// };