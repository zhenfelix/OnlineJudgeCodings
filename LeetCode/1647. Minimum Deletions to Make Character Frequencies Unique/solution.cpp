// class Solution {
// public:
//     int minDeletions(string s) {
//         vector<int> cc(26,0);
//         for (auto ch : s)
//             cc[ch-'a']++;
//         sort(cc.begin(), cc.end(), greater<>());
//         int res = 0;
//         for (int i = 0; i < 26; i++){
//             if (cc[i] == 0)
//                 continue;
//             for (int j = i+1; j < 26 && cc[j] == cc[i]; j++){
//                 res++;
//                 cc[j]--;
//             }
//         }
//         return res;
//     }
// };

class Solution {
public:
    int minDeletions(string s) {
        vector<int> cnt(26, 0);
        for (auto ch: s) {
            cnt[ch - 'a']++;
        }
        sort(cnt.begin(), cnt.end(), greater<int>());
        
        int ret = 0;
        int prev = cnt[0];
        for (int i = 1; i < 26 && cnt[i] > 0; i++) {
            if (prev <= cnt[i]) {
                prev = max(prev - 1, 0);
                ret += (cnt[i] - prev);
            } else {
                prev = cnt[i];
            }
        }
        return ret;
    }
};


// 作者：Arsenal-591
// 链接：https://leetcode-cn.com/problems/minimum-deletions-to-make-character-frequencies-unique/solution/tan-xin-on-suan-fa-by-arsenal-591/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。