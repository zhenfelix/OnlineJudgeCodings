class Solution:
    def evaluate(self, expression: str) -> int:
        def expr(i,var):
            i += 1
            op = ""
            while expression[i] != " ":
                op += expression[i]
                i += 1
            i += 1
            res = []
            if op in ["add", "mult"]:
                for _ in range(2):
                    if expression[i] == "(":
                        tmp, i = expr(i,var.copy())
                        res.append(tmp)
                    else:
                        token = ""
                        while expression[i] not in [" ", ")"]:
                            token += expression[i]
                            i += 1
                        if token and (token[0].isdigit() or token[0] == "-"):
                            res.append(int(token))
                        else:
                            res.append(var[token])
                    while expression[i] == " ":
                        i += 1
            else:
                var_pre = ""
                while expression[i] != ")":
                    if expression[i] == "(":
                        tmp, i = expr(i,var.copy())
                        res.append(tmp)
                        if var_pre:
                            var[var_pre] = res[-1]
                            var_pre = ""
                    else:
                        token = ""
                        while expression[i] not in [" ", ")"]:
                            token += expression[i]
                            i += 1
                        if token and (token[0].isdigit() or token[0] == "-"):
                            res.append(int(token))
                            if var_pre:
                                var[var_pre] = res[-1]
                                var_pre = ""
                        else:
                            var_pre = token
                    while expression[i] == " ":
                        i += 1
            # print(op,i,expression[i],var,res)
            if op == "add":
                return res[0]+res[1], i+1
            elif op == "mult":
                return res[0]*res[1], i+1
            else:
                return res[-1], i+1

        return expr(0,{})[0]