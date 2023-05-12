// leetcode 43. Multiply Strings

#include <string>
#include<vector>
using namespace std;


class Solution
{
public:
    string multiply(string num1, string num2)
    {
        int n1 = num1.length(), n2 = num2.length();
        std::vector<int> v1(n1), v2(n2), ans(n1 + n2, 0);
        for (int i = n1 - 1; i >= 0; i--)
            v1[n1 - 1 - i] = num1[i] - '0';
        for (int i = n2 - 1; i >= 0; i--)
            v2[n2 - 1 - i] = num2[i] - '0';
        for (int i = 0; i < n1; i++)
        {
            int carry = 0;
            for (int j = 0; j < n2; j++)
            {
                ans[i + j] += v1[i] * v2[j] + carry;
                carry = ans[i + j] / 10;
                ans[i + j] %= 10;
            }
            ans[i + n2] = carry;
        }
        string s;
        bool zero = true;
        for (int i = n1 + n2 - 1; i >= 0; i--)
        {
            if (ans[i])
                zero = false;
            if (ans[i] == 0 && zero)
                continue;
            s.push_back(ans[i] + '0');
        }
        return s.empty() ? "0" : s;
    }
};