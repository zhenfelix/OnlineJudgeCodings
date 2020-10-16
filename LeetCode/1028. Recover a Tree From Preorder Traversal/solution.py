# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        self.idx = 0
        vals = []
        depth = []
        dash, cnt, val = True, 0, ''
        for ch in S+'-':
            if ch == '-':
                if not dash:
                    vals.append(int(val))
                    val = ''
                    dash = True
                cnt += 1
            else:
                if dash:
                    depth.append(cnt)
                    cnt = 0
                    dash = False
                val += ch
        n = len(depth)


        # def dfs(d):
        #     root = None
        #     if self.idx == n or d > depth[self.idx]:
        #         return root
        #     if d == depth[self.idx]:
        #         root = TreeNode(vals[self.idx])
        #         self.idx += 1
        #     root.left = dfs(d+1)
        #     root.right = dfs(d+1)
        #     return root

        st = []
        d = 0
        # print(depth,vals)
        for dep, val in zip(depth,vals):
            while len(st) > dep:
                tmp = st.pop()
                if st:
                    if not st[-1].left:
                        st[-1].left = tmp
                    else:
                        st[-1].right = tmp
            st.append(TreeNode(val))
            # print(dep,val,st)
        while len(st) > 1:
            tmp = st.pop()
            if st:
                if not st[-1].left:
                    st[-1].left = tmp
                else:
                    st[-1].right = tmp

        return st[0]

            
