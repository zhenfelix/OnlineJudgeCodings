// class Solution {
// public:
    
//     int trailingZeroes(int n) {
//         int ans=0,step=5,pstep=1;
//         while(step/5==pstep&&n/step>0){
//             ans+=(n/step);
//             pstep=step;
//             step*=5;
//         }
//         return ans;
//     }
// };

class Solution {
public:
    
    int trailingZeroes(int n) {
        int ans=0;
        while(n!=0){
            n/=5;
            ans+=n;
        }
        return ans;
    }
};