#include <vector>
#include <string>
#include <stack>
#include <map>
#include <algorithm>
using namespace std;

// class Solution {
// public:
//     void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
//         vector<int> tmp;
//         for(int i=0;i<m;i++)tmp.push_back(nums1[i]);
//         int i=0,j=0;
//         for(;i<m&&j<n;){
            
//             if(tmp[i]<nums2[j]){
//                 nums1[i+j]=tmp[i];
//                 i++;
//             }
//             else{
//                 nums1[i+j]=nums2[j];
//                 j++;
//             }
//         }
//         for(;i<m||j<n;){
//             if(i==m){
//                 nums1[i+j]=nums2[j];
//                 j++;
//             }
//             else {
//                 nums1[i+j]=tmp[i];
//                 i++;
//             }
//         }
//     }
// };

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i=m-1,j=n-1,k=m+n-1;
        while(j>=0&&i>=0){
            if(nums1[i]<nums2[j])nums1[k--]=nums2[j--];
            else nums1[k--]=nums1[i--];
        }
        while(j>=0)nums1[k--]=nums2[j--];
    }
};

