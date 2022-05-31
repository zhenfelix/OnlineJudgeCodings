证明：考虑在构造时候的最优解序列是...xy...对应的x和y在字符串中的位置分类讨论一下

class Solution {
public:
    int minMovesToMakePalindrome(string s) {
        int n = s.size(), ans = 0;
        for (int i = 0, j = n - 1; i < j; i++) {
            for (int k = j; i != k; k--) if (s[i] == s[k]) {
                // 字母出现偶数次的情况，模拟交换
                for (; k < j; k++) swap(s[k], s[k + 1]), ans++;
                j--;
                goto OK;
            }
            // 字母出现奇数次的情况，计算它距离中间还有多少距离
            ans += n / 2 - i;
            OK: continue;
        }
        return ans;
    }
};


作者：tsreaper
链接：https://leetcode-cn.com/problems/minimum-number-of-moves-to-make-palindrome/solution/tan-xin-zheng-ming-geng-da-shu-ju-fan-we-h57i/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。