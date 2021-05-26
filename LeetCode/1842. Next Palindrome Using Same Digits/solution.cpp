class Solution {
public:
    string nextPalindrome(string num) {
        int n = num.size();
        string hi = num.substr(0,n/2);
        string lo = hi;
        reverse(lo.begin(), lo.end());
        string mid = num.substr(n/2,n%2);

        string lo_nxt = lo;
        bool lo_flag = next_permutation(lo_nxt.begin(), lo_nxt.end());
        string lo_nxt_hi = lo_nxt;
        reverse(lo_nxt_hi.begin(), lo_nxt_hi.end());
        string res1 = lo_flag ? lo_nxt_hi+mid+lo_nxt_hi : "";
        res1 = res1 > num ? res1 : "";

        string hi_nxt = hi;
        bool hi_flag = next_permutation(hi_nxt.begin(), hi_nxt.end());
        string hi_nxt_lo = hi_nxt;
        reverse(hi_nxt_lo.begin(), hi_nxt_lo.end());
        string res2 = hi_flag ? hi_nxt+mid+hi_nxt_lo : "";
        res2 = res2 > num ? res2 : "";
        if (res1.size() && res2.size())
            return min(res1, res2);
        return res1.size() ? res1 : res2;

    }
};