// class Solution {
// public:
//     string replaceDigits(string s) {
//         string res;
//         int n = s.size();
//         for (int i = 0; i < n; i += 2){
//             res.push_back(s[i]);
//             if (i+1 < n)
//                 res.push_back(s[i]+s[i+1]-'0');
//         }
//         return res;
//     }
// };

///Anany O(N)
class Solution {
public:
    string replaceDigits(string s) {
        for(int i = 1; i < s.size(); i += 2) {
            s[i] = s[i-1] + (s[i] - '0');
        }
        return s;
    }
};