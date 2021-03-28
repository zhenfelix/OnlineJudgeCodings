class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        res = []
        tmp = []
        flag = False
        knowledge = {k: v for k, v in knowledge}
        for ch in s:
            if ch == "(":
                flag = True
            elif ch == ")":
                key = ''.join(tmp)
                tmp = []
                flag = False
                if key in knowledge:
                    res.append(knowledge[key])
                else:
                    res.append("?")
            elif flag:
                tmp.append(ch)
            else:
                res.append(ch)
        return ''.join(res)