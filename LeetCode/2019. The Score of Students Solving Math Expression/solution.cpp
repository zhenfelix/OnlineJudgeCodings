using ll = long long;

unordered_map<char, int> order = {{'#', -1}, {'+', 1}, {'-', 1}, {'*', 2}, {'/', 2}, {'$', 0}, {'(', 0}};

// Leetcode 224: Basic Calculator
class Calculator {
    string trim(string s) {
        string t;
        for (char c : s)
            if (c != ' ')
                t.push_back(c);
        return t;
    }
    
    ll calc(ll a, ll b, char c) {
        switch(c) {
            case '+':
                return a + b;
            case '-':
                return a - b;
            case '*':
                return a * b;
            case '/':
                return a / b;
            default:
                return a;
        }
    }
public:
    int calculate(string s) {
        s = trim(s);
        stack<ll> val;
        stack<char> op;
        op.push('#');
        bool is_num = false, is_negative = false;
        ll num = 0;
        s += '$';
        auto work = [&](){
            ll b = val.top();
            val.pop();
            ll a = val.top();
            val.pop();
            val.push(calc(a, b, op.top()));
            op.pop();
        };
        for (int i = 0; i < s.size(); ++i) {
            char c = s[i];
            ll delta = c - '0';
            if (delta >= 0 && delta <= 9) {
                num = num * 10 + delta;
                is_num = true;                
            }
            else {
                if (is_num) {
                    val.push(is_negative ? -num : num);
                    is_num = false;
                    is_negative = false;
                } else {
                    if (c == '-' && (i == 0 || s[i - 1] != ')')) {
                        is_negative = true;
                        continue;
                    }
                }

                // Special case: "-(...)" => "-1*(...)"
                if (is_negative) {
                    val.push(-1);
                    while (order[op.top()] >= order['*'])
                        work();
                    op.push('*');
                    is_negative = false;
                }

                num = 0;
                if (c == ')')
                    while (op.top() != '(')
                        work();
                else if (c != '(')
                    while (order[op.top()] >= order[c])
                        work();
                if (c == ')')
                    op.pop();
                else
                    op.push(c);
            }
        }
        return val.top();
    }
};

class Solution {
public:
    int scoreOfStudents(string s, vector<int>& answers) {
        vector<int> nums;
        vector<char> ops;
        for (char ch : s) {
            if (ch == '+' || ch == '*')
                ops.emplace_back(ch);
            else
                nums.emplace_back(ch - '0');
        }
        
        int n = nums.size();
        
        // Calculate correct answer.
        Calculator calculator;
        ll correct = calculator.calculate(s);
        
        // Calculate possible answers.
        vector<vector<unordered_set<int>>> dp(n, vector<unordered_set<int>>(n));
        for (int i = 0; i < n; ++i)
            dp[i][i].emplace(nums[i]);
        for (int len = 2; len <= n; ++len) {
            for (int i = 0; i + len - 1 < n; ++i) {
                int j = i + len - 1;
                for (int k = i; k < j; ++k) {
                    for (int x : dp[i][k])
                        for (int y : dp[k + 1][j]) {
                            if (ops[k] == '+' && x + y <= 1000)
                                dp[i][j].emplace(x + y);
                            else if (ops[k] == '*' && x * y <= 1000)
                                dp[i][j].emplace(x * y);
                        }
                }
            }
        }
        
        int ans = 0;
        for (int answer : answers) {
            if (answer == correct)
                ans += 5;
            else if (dp[0][n - 1].count(answer))
                ans += 2;
        }
        
        return ans;
    }
};


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/uxwWwd/view/rM8PFg/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。