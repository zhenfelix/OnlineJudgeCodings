// class Solution
// {
// public:
//     bool checkPalindromeFormation(string a, string b)
//     {
//         int n = a.length();
//         vector<bool> dpa(n, false), dpb(n, false);
//         int left = n / 2, right = n / 2;
//         if (n % 2 == 0)
//             left--;
//         while (left >= 0 && a[left] == a[right])
//         {
//             dpa[left] = dpa[right] = true;
//             left--;
//             right++;
//         }
//         left = n / 2, right = n / 2;
//         if (n % 2 == 0)
//             left--;
//         while (left >= 0 && b[left] == b[right])
//         {
//             dpb[left] = dpb[right] = true;
//             left--;
//             right++;
//         }
//         if (dpa[0] || dpb[0])
//             return true;
//         for (int left = 0, right = n - 1; a[left] == b[right]; left++, right--)
//         {
//             if (dpa[left + 1] || dpb[left + 1] || left + 1 > right - 1)
//                 return true;
//         }
//         for (int left = 0, right = n - 1; b[left] == a[right]; left++, right--)
//         {
//             if (dpa[left + 1] || dpb[left + 1] || left + 1 > right - 1)
//                 return true;
//         }
//         return false;
//     }
// };


class Solution {
    bool check(string a, string b) {
        int n = a.size();
        bool flag = true;
        for (int i = 0; i < n / 2; ++i) {
            if (flag) {
                if (a[i] != b[n - 1 - i])
                    flag = false;
            }
            if (!flag)
                if (a[i] != a[n - 1 - i])
                    return false;
        }
        return true;
    }
public:
    bool checkPalindromeFormation(string a, string b) {
        if (check(a, b) || check(b, a))
            return true;
        reverse(a.begin(), a.end());
        reverse(b.begin(), b.end());
        if (check(a, b) || check(b, a))
            return true;
        return false;
    }
};


// 作者：lucifer1004
// 链接：https://leetcode-cn.com/problems/split-two-strings-to-make-palindrome/solution/jiao-huan-dao-xu-wo-men-ju-jue-fen-qing-kuang-tao-/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。