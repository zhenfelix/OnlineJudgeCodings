// class Solution {
// public:
//     bool great(string s1, string s2){
//         int n = s1.length();
//         for (int i = 0; i < n; i++)
//             if (s1[i] < s2[i])
//                 return false;
//         return true;
//     }
//     bool checkIfCanBreak(string s1, string s2) {
//         sort(s1.begin(), s1.end());
//         sort(s2.begin(), s2.end());
//         return great(s1,s2) || great(s2,s1);
//     }
// };


class Solution {
public:
    bool check(string s1, string s2) {
        int book1[27] = {0}, book2[27] = {0};
        for (auto p: s1) {
            book1[p - 'a']++;
        }
        // 检查s1能不能打击s2
        for(auto p: s2) {
            // 找一个最省力的s1中元素
            for (int i = p - 'a'; i <= 'z' - 'a'; i++) {
                if (book1[i] > 0) {
                    book1[i]--; // 用掉一个元素
                    break;
                }
                if (i == 'z' - 'a') {
                    return false; // 出错！
                }
            }
        }
        return true;
    }
    bool checkIfCanBreak(string s1, string s2) {
        return check(s1, s2) || check(s2, s1);
    }
};
