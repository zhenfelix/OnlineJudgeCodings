class Solution {
public:
    bool validPalindrome(string s) {
        function<bool(int,int,int)> check = [&](int left, int right, int cnt){
            if (left >= right)
                return true;
            if (s[left] == s[right])
                return check(left+1, right-1, cnt);
            if (cnt > 0)
                return check(left+1, right, cnt-1) || check(left, right-1, cnt-1);
            return false;
        };
        return check(0, s.length()-1, 1);
    }
};