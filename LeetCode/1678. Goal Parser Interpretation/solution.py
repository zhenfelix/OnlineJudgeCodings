class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        n = len(command)
        for i in range(n):
            if command[i] == '(':
                if command[i+1] == ')':
                    res += 'o'
            elif command[i] == ')':
                pass
            else:
                res += command[i]
        return res 


class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()','o').replace('(al)','al')