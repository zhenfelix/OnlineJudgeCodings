class Solution:
    # def simplifyPath(self, path: str) -> str:
    #     path = path.split("/")
    #     st = ['']
    #     for p in path:
    #         if p in ['','.']:
    #             continue
    #         elif p == '..':
    #             if len(st) > 1:
    #                 st.pop()
    #         else:
    #             st.append(p)
    #     return "/".join(st) or "/"
    
    
    def simplifyPath(self, path):
        stack = []
        for p in path.split("/"):
            if p == "..":
                if stack:
                    stack.pop()
            elif p and p != '.':
                stack.append(p)
        return '/' + '/'.join(stack)