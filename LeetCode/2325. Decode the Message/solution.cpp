class Solution {
public:
    string decodeMessage(string key, string message) {
        int ord[26] = {0}, cnt = 0;
        for (char c : key) if (c >= 'a' && c <= 'z' && ord[c - 'a'] == 0) ord[c - 'a'] = ++cnt;
        for (char &c : message) if (c >= 'a' && c <= 'z') c = ord[c - 'a'] - 1 + 'a';
        return message;
    }
};


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/S2zplk/view/oXXn3g/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。