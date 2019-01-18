#include <vector>
#include <string>
#include <stack>
#include <map>
#include <algorithm>
using namespace std;

// class Solution {
// public:
//     string Generate(string x,int n){
//         if(n==1)return x;
//         string ans="";
//         int cc=0;char pre=x[0];
//         for(int i=0;i<=x.size();i++){
//             if(i==x.size()||x[i]!=pre){
//                 ans+=('0'+cc);
//                 ans+=pre;
//                 if(i==x.size())break;
//                 cc=1;
//                 pre=x[i];
//             }
//             else{
//                 cc++;
//                 pre=x[i];
//             }
//         }
//         return Generate(ans, n-1);
//     }
//     string countAndSay(int n) {
//         return Generate("1", n);
//     }
// };

class Solution{
    public:
    string countAndSay(int n) {
    if (n == 0) return "";
    string res = "1";
    while (--n) {
        string cur = "";
        for (int i = 0; i < res.size(); i++) {
            int count = 1;
             while ((i + 1 < res.size()) && (res[i] == res[i + 1])){
                count++;    
                i++;
            }
            cur += to_string(count) + res[i];
        }
        res = cur;
    }
    return res;
}
    
};
