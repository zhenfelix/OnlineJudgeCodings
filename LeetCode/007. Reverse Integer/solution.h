#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

// class Solution {
// public:
//     int reverse(int x) {
//         bool flag=true;
//         if(x<0){
//             flag=false;
//             x=-x;
//             if(x<0)return 0;
//         }
//         long long ans=0;
//         while(x){
//             int tmp=x%10;
//             x=x/10;
//             ans=tmp+10*ans;
            
//         }
//         long long base=1;
//         long long INF=(base<<31);
// //        printf("%lld",INF);
//         if(ans>INF)return 0;
//         int ans_=ans;
//         return flag?ans_:(-ans_);
//     }
// };


class Solution {
public:
    int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            if (rev < INT_MIN / 10 || rev > INT_MAX / 10) {
                return 0;
            }
            int digit = x % 10;
            x /= 10;
            rev = rev * 10 + digit;
        }
        return rev;
    }
};


// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/reverse-integer/solution/zheng-shu-fan-zhuan-by-leetcode-solution-bccn/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

// class Solution {
// public:
//     int reverse(int x) {
//         int num=x;
//         int sum=0;
//         int pnum=0;
//         while(num)
//         {
//             int temp=num%10;
//             sum=sum*10+temp;
//             if(sum/10!=pnum)//determine whethere it is reversible
//                 return 0;
//             pnum=sum;
//             num=num/10;
//         }
//         return sum;
//     }
// };