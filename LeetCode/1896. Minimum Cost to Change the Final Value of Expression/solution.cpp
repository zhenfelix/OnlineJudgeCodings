class Solution {
public:
    int minOperationsToFlip(string expression) {
        int cur = 0;
        vector<int> depth, val, dp;
        vector<char> ops;
        for (auto ch : expression){
            if (ch == '('){
                cur++;
            }
            else if (ch == ')'){
                cur--;
                depth.back()--;
            }
            else if (ch == '|' || ch == '&'){
                ops.push_back(ch);
            }
            else{
                val.push_back(ch-'0');
                dp.push_back(1);
                depth.push_back(cur);
            }
            int n = depth.size();
            if (n >= 2 && depth[n-1] == depth[n-2]){
                depth.pop_back();
                char op = ops.back(); ops.pop_back();
                int a = val.back(); val.pop_back();
                int b = val.back(); val.pop_back();
                int x = dp.back(); dp.pop_back();
                int y = dp.back(); dp.pop_back();
                if (a^b){
                    dp.push_back(1);
                }
                else{
                    dp.push_back(min(x,y)+((a==1)^(op=='&')));
                }
                if (op == '&'){
                    val.push_back(a&b);
                }
                else{
                    val.push_back(a|b);
                }
            }
        }
        return dp.back();
    }
};