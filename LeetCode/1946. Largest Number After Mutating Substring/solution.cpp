class Solution {
public:
    string maximumNumber(string num, vector<int>& change) {
        int n = num.size(), i = 0;
        while (i < n && change[num[i] - '0'] <= num[i] - '0')
            i++;
        while (i < n && change[num[i] - '0'] >= num[i] - '0')
            num[i] = change[num[i] - '0'] + '0', i++;
        return num;
    }
};

// 作者：吴自华
// 链接：https://leetcode-cn.com/circle/discuss/zesmlZ/view/SqRxlN/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。