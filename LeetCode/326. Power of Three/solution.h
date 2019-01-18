// class Solution {
// public:
//     bool isPowerOfThree(int n) {
//         if(n<1)return false;
//         if(n==1)return true;
//         int s=sqrt(n);
//         if(s*s==n)return isPowerOfThree(s);
//         else if(n%3==0)return isPowerOfThree(n/3);
//         else return false;
//     }
// };

class Solution{
    public:
    bool isPowerOfThree(int n){
        while(n>=1){
            if(n==1)return true;
            int s=sqrt(n);
            if(s*s==n)n=s;
            else if(n%3==0) n=n/3;
            else return false;
        }
        return false;
    }
};

// class Solution {
// public:
//     bool isPowerOfThree(int n) {
//         int maxPowerOfThree = 1162261467;//3^19, while 3^20 > INT_MAX;
        
//         if(n <= 0 || n > maxPowerOfThree)
//             return false;
//         return maxPowerOfThree % n == 0;
//     }
// };
// static const auto __ = []() {
//     std::ios::sync_with_stdio(false);
//     std::cin.tie(nullptr);
//     return nullptr;
// }();