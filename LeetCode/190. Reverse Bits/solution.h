class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t m=0;
        int i=32;
        while(i--){
            m=(m<<1);
            if(n&1)m=m|1;
            n=(n>>1);
        }
        return m;
    }
};