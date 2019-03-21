// class Solution {
// public:

//     bool repeatedSubstringPattern(string s) {
//         int n=s.length();
//         int i=0,j=1;
//         while(j<=n/2){
//             i=0;
//             if(n%j==0){
//                 for(i=j;i<n;i+=j){
//                     if(s.substr(0,j)!=s.substr(i,j))break;
//                 }
//                 if(i>=n)return true;
                
//             }
//             j++;
//         }
//         return false;
//     }
// };

class Solution {
public:

    bool repeatedSubstringPattern(string str) 
    {
        return (str + str).substr(1, str.size() * 2 - 2).find(str)!=-1;
    }
};


//new_str = pattern_wo_head + (2m-2) * pattern + pattern_wo_rear 
//https://leetcode.com/problems/repeated-substring-pattern/discuss/94360/My-one-line-c++-solution