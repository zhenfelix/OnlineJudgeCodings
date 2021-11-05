# 1，当str1 == str2时显然可以转化
# 2，如果str1 != str2，如果str2包含所有的26个字母，则没有了操作空间，因此肯定不能转化
# 3，如果str1某两个下标i, j对应的字符相同，则必须要求str2中的相同下标也必须相同
# 如果判断以上情况后没有问题，则可以转化成功

# 作者：da-li-wang
# 链接：https://leetcode-cn.com/problems/string-transforms-into-another-string/solution/c-jian-dan-bian-li-ji-ke-by-da-li-wang/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution {
public:
    bool canConvert(string str1, string str2) {
        if (str1 == str2)
            return true;
        int n = str1.size();
        vector<int> mp(26, -1), rmp(26, -1);
        bool branch = false;
        for (int i = 0; i < n; i++){
            int a = str1[i]-'a', b = str2[i]-'a';
            if (mp[a] != -1 && mp[a] != b)
                return false;
            if (rmp[b] != -1 && rmp[b] != a)
                branch = true;
            mp[a] = b;
            rmp[b] = a;
        }
        if (branch)
            return true;
        for (int j = 0; j < 26; j++){
            // cout << j << " " << mp[j] << endl;
            if (mp[j] == -1)
                return true;
        }
            
        return false;
    }
};




class Solution {
public:
    bool canConvert(string str1, string str2) {
        if (str1 == str2)
            return true;
        int n = str1.size();
        vector<int> mp(26, -1), rmp(26, -1);
        for (int i = 0; i < n; i++){
            int a = str1[i]-'a', b = str2[i]-'a';
            if (mp[a] != -1 && mp[a] != b)
                return false;
            mp[a] = b;
            rmp[b] = a;
        }

        for (int j = 0; j < 26; j++){
            // cout << j << " " << mp[j] << endl;
            if (rmp[j] == -1)
                return true;
        }
            
        return false;
    }
};