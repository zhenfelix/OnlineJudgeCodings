class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        res = [0]*(len(num1)+len(num2))
        for i, a in enumerate(num1[::-1]):
            for j, b in enumerate(num2[::-1]):
                res[i+j] += int(a)*int(b)
        carry = 0
        for idx, cur in enumerate(res):
            res[idx], carry = (cur+carry)%10, (cur+carry)//10
        ans = ''.join([str(x) for x in res[::-1]])
        if ans[0] == '0':
            ans = ans[1:]
        return ans

