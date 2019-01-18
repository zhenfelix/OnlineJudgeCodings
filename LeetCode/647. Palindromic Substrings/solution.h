// class Solution {
// public:
//     int countSubstrings(string s) {
//         int n=s.length(),cc=n;
//         vector<bool> pre(n,true),cur(n,true);
//         for(int len=2;len<=n;len++){
//             for(int i=0;i+len<=n;i++){
//                 if(s[i]==s[i+len-1]&&pre[i+1]){
//                     pre[i]=cur[i];
//                     cur[i]=true;
//                     cc++;
//                 }
//                 else{
//                     pre[i]=cur[i];
//                     cur[i]=false;
//                 }
//             }
//         }
//         return cc;
//     }
// };

class Solution {
public:
    int countSubstrings(string s) {
        int res = 0, n = s.length();
        for(int i = 0; i < n; i++){
            for(int j = 0; i-j >= 0 && i+j < n && s[i-j] == s[i+j]; j++)res++; //substring s[i-j, ..., i+j]
            for(int j = 0; i-1-j >= 0 && i+j < n && s[i-1-j] == s[i+j]; j++)res++; //substring s[i-1-j, ..., i+j]
        }
        return res;
    }
};


