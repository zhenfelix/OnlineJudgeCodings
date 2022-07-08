# 同 1597. 根据中缀表达式构造二叉表达式树
class Solution:
    def calculate(self, s: str) -> int:
        s = '('+s+')'
        ops, st = [], []
        mp = {'(':-1, ')':-1, '-':0, '+':0, '*':1, '/':1}
        tmp = []
        def calc(op, l, r):
            if op == '+':
                return l+r 
            elif op == '-':
                return l-r
            elif op == '/':
                res = abs(l)//abs(r)
                return -res if l*r < 0 else res
            else:
                return l*r 

        for ch in s:
            if ch not in mp:
                tmp.append(ch)                
            else:
                if tmp:
                    st.append(int(''.join(tmp)))
                    tmp = []
                if ch == '(':
                    ops.append(ch)
                    continue
                while ops and mp[ch] <= mp[ops[-1]]:
                    op = ops.pop()
                    if op == '(':
                        break
                    r = st.pop()
                    l = st.pop() 
                    st.append(calc(op,l,r))
                if ch != ')':
                    ops.append(ch)
        return st[-1]



# class Solution:
#     def calculate(self, s: str) -> int:
#         def express(nums_, ops_):
#             # print(nums_)
#             # print(ops_)
#             st_nums, st_ops = [nums_[0]], []
#             for i, op in enumerate(ops_):
#                 if op in "+-":
#                     st_nums.append(nums_[i+1])
#                     st_ops.append(op)
#                 elif op == "*":
#                     st_nums[-1] *= nums_[i+1]
#                 elif op == "/":
#                     st_nums[-1] //= nums_[i+1]
#             nums_, ops_ = st_nums, st_ops
#             res = nums_[0]
#             for i, op in enumerate(ops_):
#                 if op == '+':
#                     res += nums_[i+1]
#                 else:
#                     res -= nums_[i+1]
#             return res

#         nums, ops, brackets = [], [], []
#         cur = ''
#         negative = False
#         for ch in s+' ':
#             if ch < '0' or ch > '9':
#                 if cur:
#                     num = int(cur)
#                     if negative:
#                         num = -num
#                         negative = False
#                     cur = ''
#                     nums.append(num)
#                 if ch in "+-/*":
#                     if len(ops) == len(nums):
#                         negative = True
#                     else:
#                         ops.append(ch)
                    
#                 elif ch == '(':
#                     brackets.append(len(ops))
#                 elif ch == ')':
#                     idx = brackets.pop()
#                     num = express(nums[idx:],ops[idx:])
#                     while len(nums) > idx:
#                         nums.pop()
#                     while  len(ops) > idx:
#                         ops.pop()
#                     nums.append(num)
#             else:
#                 cur += ch
#         return express(nums,ops)