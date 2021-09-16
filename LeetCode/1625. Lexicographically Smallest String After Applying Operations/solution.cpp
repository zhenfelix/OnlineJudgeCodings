class Solution {
    int gcd(int x, int y) {
        return y == 0 ? x : gcd(y, x % y);
    }
public:
    string findLexSmallestString(string s, int a, int b) {
        int n = s.size();
        string ans = s;
        string t = s + s;
        int ga = gcd(10, a), gb = gcd(n, b);
        
        // 奇偶通用的add操作
        auto add = [&](string &p, int pos) {
            int lo = p[pos] - '0', added = 0;
            for (int i = ga; i < 10; i += ga) {
                int c = (p[pos] - '0' + i) % 10;
                if (c < lo) {
                    lo = c;
                    added = i;
                }
            }
            if (added)
                for (int i = pos; i < n; i += 2)
                    p[i] = '0' + (p[i] - '0' + added) % 10;
        };
        
        // rotate操作
        for (int i = 0; i < n; i += gb) {
            string p = t.substr(i, n);
            add(p, 1);
            if (gb % 2)
                add(p, 0);
            ans = min(ans, p);
        }
        return ans;
    }
};


// 作者：lucifer1004
// 链接：https://leetcode-cn.com/problems/lexicographically-smallest-string-after-applying-operations/solution/bao-li-mei-xue-by-lucifer1004/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

// class Solution {
//     int gcd(int x, int y) {
//         return y == 0 ? x : gcd(y, x % y);
//     }
// public:
//     string findLexSmallestString(string s, int a, int b) {
//         int n = s.size();
//         string ans = s;
//         string t = s + s;
//         int g = gcd(n, b);
//         for (int i = 0; i < n; i += g) {
//             string p = t.substr(i, n);
//             for (int j = 0; j <= 9; ++j) {
//                 int th = g % 2 == 0 ? 0 : 9;
//                 for (int k = 0; k <= th; ++k) {
//                     string q(p);
//                     for (int t = 1; t < n; t += 2)
//                         q[t] = '0' + (q[t] - '0' + a * j) % 10;
//                     for (int t = 0; t < n; t += 2)
//                         q[t] = '0' + (q[t] - '0' + a * k) % 10;
//                     ans = min(ans, q);
//                 }
//             }
//         }
//         return ans;
//     }
// };


// 作者：lucifer1004
// 链接：https://leetcode-cn.com/problems/lexicographically-smallest-string-after-applying-operations/solution/bao-li-mei-xue-by-lucifer1004/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


// class Solution {
// public:
//     string findLexSmallestString(string s, int a, int b) {
//         int n = s.length();
//         string res = s;
//         for (int odd = 0; odd <= 9*a; odd += a){
//             for (int even = 0; even <= 9*a; even += a){
//                 for (int i = 0; i <= b*n; i += b){
//                     string ss = s;
//                     for (int j = 0; j < n; j++){
//                         if (j&1)
//                             ss[j] = (ss[j]-'0'+odd)%10 + '0';
//                         else
//                             ss[j] = (ss[j]-'0'+even)%10 + '0';
//                     }
//                     ss = ss.substr(i%n) + ss.substr(0,i%n);
//                     if (ss < res)
//                         res = ss;
//                 }
//                 if (b%2 == 0)
//                     break;
//             }
//         }
//         return res;
//     }
// };