class Solution:
    def calculate(self, s: str) -> int:
        s += ' '
        nums, ops = [], []
        cur = ''
        for i, ch in enumerate(s):
            if ch < '0' or ch > '9':
                if cur:
                    num = int(cur)
                    cur = ''
                    if ops and ops[-1] in ['*','/']:
                        if ops[-1] == '*':
                            nums[-1] *= num
                        else:
                            nums[-1] //= num
                        ops.pop()
                    else:
                        nums.append(num)
                if ch != ' ':
                    ops.append(ch)
            else:
                cur += ch
        ans = nums[0]
        # print(nums)
        # print(ops)
        for i, op in enumerate(ops):
            if op == '-':
                ans -= nums[i+1]
            else:
                ans += nums[i+1]
        return ans
