class Solution:
    def minOperationsToFlip(self, expression: str) -> int:

        st = [[]]
        ops = []
        expression = '('+expression+')'
        n = len(expression)
        for i in range(n)[::-1]:
            ch = expression[i]
            # print(ch,st,ops)
            if ch == ')':
                st.append([])
            elif ch == '(':
                while len(st[-1]) >= 2:
                    lc, lv = st[-1].pop()
                    rc, rv = st[-1].pop()
                    op = ops.pop()
                    if op == '&':
                        if (lv ^ rv) == 0:
                            change = min(lc,rc)+(1-lv)
                        else:
                            change = 1
                        value = (lv&rv)
                    else:
                        if (lv ^ rv) == 0:
                            change = min(lc,rc)+lv
                        else:
                            change = 1
                        value = (lv|rv)
                    st[-1].append((change,value))
                tmp = st.pop()[-1]
                st[-1].append(tmp)

                
            elif ch in ['0','1']:
                st[-1].append((1,int(ch)))
            else:
                ops.append(ch)
        return st[-1][0][0]



