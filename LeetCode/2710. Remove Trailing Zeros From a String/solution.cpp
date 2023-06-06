class Solution {
public:
    string removeTrailingZeros(string num) {
        while (!num.empty() && num.back() == '0') num.pop_back();
        return num;
    }
};

作者：TsReaper
链接：https://leetcode.cn/circle/discuss/5eR2p8/view/Acz0TI/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。