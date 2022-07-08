class Solution {
public:
    string discountPrices(string sentence, int discount) {
        string res;
        istringstream iss(sentence);
        string t;
        while (getline(iss, t, ' ')) { // while (iss >> t)
            bool isPrice = (t.size() > 1 && t[0] == '$');
            if (isPrice) {
                for (int i = 1; i < t.size(); ++i) {
                    if (t[i] == '$' || t[i] < '0' || t[i] > '9') {
                        isPrice = 0; break;
                    }
                }
            }
            if (isPrice) {
                string p = t.substr(1);
                double price = stod(p);
                price *= (100 - discount) * 0.01;
                
                ostringstream oss;
                oss << fixed << setprecision(2) << price;
                
                res += '$' + oss.str() + ' ';
            } else {
                res += t + ' ';
            }
        }
        res.pop_back();
        return res;
    }
};


// 作者：mfk443838746
// 链接：https://leetcode.cn/problems/apply-discount-to-prices/solution/c-by-mfk443838746-28qy/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution {
public:
    string discountPrices(string sentence, int discount) {
        string res;
        stringstream iss(sentence);
        string t;
        while (getline(iss, t, ' ')) { // while (iss >> t)
            bool isPrice = (t.size() > 1 && t[0] == '$');
            if (isPrice) {
                for (int i = 1; i < t.size(); ++i) {
                    if (t[i] == '$' || t[i] < '0' || t[i] > '9') {
                        isPrice = 0; break;
                    }
                }
            }
            if (isPrice) {
                string p = t.substr(1);
                double price = stod(p);
                price *= (100 - discount) * 0.01;
                
                stringstream oss;
                oss.precision(2);
                oss << fixed << price;
                
                res += '$' + oss.str() + ' ';
            } else {
                res += t + ' ';
            }
        }
        res.pop_back();
        return res;
    }
};




class Solution {
public:
    string discountPrices(string sentence, int discount) {
        string ret;
        for(int i = 0, j = 0; i <= sentence.size(); ++i) {
            if(i == sentence.size() || sentence[i] == ' ') {
                string s = sentence.substr(j, i-j);
                bool price = false;
                if(s[0] == '$' && s.size() > 1) {
                    bool isnum = true;
                    for(int k = 1; k < s.size(); ++k)
                        if(!isdigit(s[k])) isnum = false;
                    if(isnum) price = true;
                }
                if(price) {
                    long long after = stoll(s.substr(1)) * (100 - discount);
                    char tmp[20];
                    sprintf(tmp, "$%lld.%02lld", after / 100, after % 100);
                    ret += tmp;
                    ret += " ";
                } else {
                    ret += s;
                    ret += " ";
                }
                j = i+1;
            }
        }
        ret.pop_back();
        return ret;
    }
};


// 作者：newhar
// 链接：https://leetcode.cn/problems/apply-discount-to-prices/solution/c-hao-nan-a-dan-shi-huan-shi-yao-xie-ge-bzosn/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。