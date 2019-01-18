// class Solution {
// public:
//     bool isPowerOfFour(int num) {
//         return num > 0 && (num & (num - 1)) == 0 && (num - 1) % 3 == 0;
//     }
// };

// The(num - 1) % 3 == 0is used to distinguish the 4^n from 2^n.
// 2^n = (3-1)^n = C(n,0)3^n(-1)^0+....+(-1)^n.
// 1.When 2^n is 4^n, which means n is even, in this case, (-1)^n==1 and (2^n-1）%3==0
// 2.When 2&n is not 4^n, which means n is odd, in this case, (-1)^n=-1 and (2^n-1）%3==2；
// This is why we can use(num-1)%3==0 as a condition to sperate 4^n from 2^n.


class Solution {
public:
    bool isPowerOfFour(int num) {
        return num > 0 && (num & (num - 1)) == 0 && !(num&0xaaaaaaaa);
    }
};