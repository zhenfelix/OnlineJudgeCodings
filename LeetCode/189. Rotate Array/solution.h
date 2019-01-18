#include <vector>
#include <string>
#include <queue>
#include <map>
#include <stack>
#include <algorithm>
using namespace std;

// class Solution {
// public:
//     int gcd(int a,int b){
//         if(b==0)return a;
//         int tmp=b;
//         b=a%b;
//         a=tmp;
//         return gcd(a,b);
//     }
//     void rotate(vector<int>& nums, int k) {
//         int len=nums.size();
//         k=k%len;
//         if(k==0)return;
//         int res=len%k;
//         int cycle=gcd(k,res);
//         for(int i=0;i<cycle;i++){
            
//             int j=i;
//             int tmp=nums[j];
//             while(1){
//                 if((j-k+len)%len==i)nums[j]=tmp;
//                 else nums[j]=nums[(j-k+len)%len];
//                 j=(j-k+len)%len;
//                 if(j==i)break;
//             }
//         }
//     }
// };


class Solution {
public:
    
    void rotate(vector<int>& nums, int k) {
        int len=nums.size();
        k=k%len;
        if(k==0)return;
        int j=0;
        for(int i=0;i<len;){
            
            int begin=j;
            int pre=nums[j];
            do{
                int tmp=nums[(j+k)%len];
                nums[(j+k)%len]=pre;
                pre=tmp;
                j=(j+k)%len;
                i++;
            }while(j!=begin);
            j++;
        }
    }
};
// Let `L` be the length of the target array, and `k` be step. We know that all `i+n*k` belong to the same cycle, now assume `N*k=M*L` and `N` will be the cycle length. By symmetry, we could know all cycles have the same length `N`, therefore, `L%N=0`. Next we would like to know what kind of `i+r` also belong to the cycle of `i+n*k`, in other words, there is an `n` such that `(i+n*k)%L=(i+r)%L`, then we have `(n*k)%L=r%L`, or equivalently `r=gcd(k,L)`. In conclusion, we could safely say between `i` and `i+r` are distinctively different cycles, therefore we could use `i++` everytime we finished a cycle and won't enter those cycles we have encountered!