class Solution:
    def calculate(self, s: str) -> int:
        def express(nums_, ops_):
            # print(nums_)
            # print(ops_)
            st_nums, st_ops = [nums_[0]], []
            for i, op in enumerate(ops_):
                if op in "+-":
                    st_nums.append(nums_[i+1])
                    st_ops.append(op)
                elif op == "*":
                    st_nums[-1] *= nums_[i+1]
                elif op == "/":
                    st_nums[-1] //= nums_[i+1]
            nums_, ops_ = st_nums, st_ops
            res = nums_[0]
            for i, op in enumerate(ops_):
                if op == '+':
                    res += nums_[i+1]
                else:
                    res -= nums_[i+1]
            return res

        nums, ops, brackets = [], [], []
        cur = ''
        negative = False
        for ch in s+' ':
            if ch < '0' or ch > '9':
                if cur:
                    num = int(cur)
                    if negative:
                        num = -num
                        negative = False
                    cur = ''
                    nums.append(num)
                if ch in "+-/*":
                    if len(ops) == len(nums):
                        negative = True
                    else:
                        ops.append(ch)
                    
                elif ch == '(':
                    brackets.append(len(ops))
                elif ch == ')':
                    idx = brackets.pop()
                    num = express(nums[idx:],ops[idx:])
                    while len(nums) > idx:
                        nums.pop()
                    while  len(ops) > idx:
                        ops.pop()
                    nums.append(num)
            else:
                cur += ch
        return express(nums,ops)