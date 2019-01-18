#include <vector>
#include <string>
#include <stack>
#include <map>
#include <algorithm>
using namespace std;

// class Solution {
// public:
//     int mySqrt(int x) {
//         int left=1,right=x;
//         int mid;
//         while(left<=right){
//             mid=(left+right)/2;
//             if(mid==x/mid&&mid*mid==x)return mid;
//             else if(mid>x/mid){
//                 right=mid-1;
//             }
//             else left=mid+1;
//         }
//         return right;
//     }
// };

// class Solution {
// public:
//     int mySqrt(int x) {
//         int left=1,right=x,mid=(left+right)/2;
//         while(left<=right){
//             if(mid>x/mid)right=mid-1;
//             else if(mid<x/mid)left=mid+1;
//             else return mid;
//             mid=(left+right)/2;
//         }
//         return right;
//     }
// };

class Solution {
public:
    int mySqrt(int x) {
        int left=1,right=x,mid=(left+right)/2;
        while(left<=right){
            if(mid>INT_MAX/mid||mid*mid>x)right=mid-1;
            else if(mid*mid<x)left=mid+1;
            else return mid;
            mid=(left+right)/2;
        }
        return right;
    }
};
