// class Solution {
// public:
//     void generate(int a, int b, int n, vector<string> &ans, string &tmp){
//         if(a==n&&b==n){
//             ans.push_back(tmp);
//             return;
//         }
//         if(a<n){
//             a++;tmp+='(';
//             generate(a,b,n,ans,tmp);
//             a--;tmp.erase(tmp.begin()+a+b);
//         }
//         if(b<n&&b<a){
//             b++;tmp+=')';
//             generate(a,b,n,ans,tmp);
//             b--;tmp.erase(tmp.begin()+a+b);
//         }
//         return;
//     }
//     vector<string> generateParenthesis(int n) {
//         int a=0,b=0;
//         vector<string> ans;
//         string tmp;
//         generate(a,b,n,ans,tmp);
//         return ans;
//     }
// };


class Solution {
public:
    void generate(int a, int b, int n, vector<string> &ans, string tmp){
        if(a==n&&b==n){
            ans.push_back(tmp);
            return;
        }
        if(a<n)generate(a+1,b,n,ans,tmp+'(');
        if(b<a)generate(a,b+1,n,ans,tmp+')');
        return;
    }
    vector<string> generateParenthesis(int n) {
        int a=0,b=0;
        vector<string> ans;
        generate(a,b,n,ans,"");
        return ans;
    }
};