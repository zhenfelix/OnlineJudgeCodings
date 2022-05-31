class Solution:
    def calculate(self, s: str) -> int:
        st = []
        cur = 0
        presign = '+'
        s = s+'+'
        for ch in s:
            if ch == ' ':
                continue
            elif '0' <= ch <= '9':
                cur = cur*10+int(ch)
            else:
                if presign == '+':
                    st.append(cur)
                elif presign == '-':
                    st.append(-cur)
                elif presign == '*':
                    st[-1] *= cur
                else:
                    if st[-1] >= 0:
                        st[-1] //= cur
                    else:
                        st[-1] = -(abs(st[-1])//cur)
                presign = ch
                cur = 0 
        return sum(st)


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



class Solution:
    def calculate(self, s: str) -> int:
        nums, ops = [0], []
        for ch in s:
            if ch == " ":
                continue
            elif ch in "+-*/":
                nums.append(0)
                ops.append(ch)
            else:
                nums[-1] *= 10
                nums[-1] += int(ch)
        nums2, ops2 = [nums[0]], []
        for i, op in enumerate(ops):
            if op in "-+":
                ops2.append(op)
                nums2.append(nums[i+1])
            elif op == "*":
                nums2[-1] *=  nums[i+1]
            else:
                nums2[-1] //= nums[i+1]
        res = nums2[0]
        for i, op in enumerate(ops2):
            if op == "-":
                res -= nums2[i+1]
            else:
                res += nums2[i+1]
        return res