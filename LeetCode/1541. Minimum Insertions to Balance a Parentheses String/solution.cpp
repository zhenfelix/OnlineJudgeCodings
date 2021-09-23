class Solution {
public:
    int minInsertions(string s) {
        int res = 0, left = 0, right = 0;
        s.push_back('$');
        for (auto ch : s){
            if (ch == '(' || ch == '$'){
                if (right){
                    right--;
                    res++;
                    if (left)
                        left--;
                    else
                        res++;
                }
                if (ch == '(')
                    left++;
            }
            else{
                right++;
                if (right%2 == 0){
                    right -= 2;
                    if (left)
                        left--;
                    else
                        res++;
                }
            }
        }
        res += left*2;
        return res;
    }
};