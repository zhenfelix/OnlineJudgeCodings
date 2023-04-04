class Solution {
public:
    int add(unsigned int a, unsigned int b) {
        while (a){
            int ta = a;
            a &= b;
            a <<= 1;
            b ^= ta;
        }
        return b;

    }
};