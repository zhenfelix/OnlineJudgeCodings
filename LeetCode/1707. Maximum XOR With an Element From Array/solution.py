class Node:
    def __init__(self):
        self.child = [None, None]

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        idx = sorted([i for i in range(len(queries))], key=lambda x: queries[x][-1])
        root = Node()
        pos = 0
        ans = [-1]*len(queries)
        def insert(val):
            cur = root
            for bit in range(32)[::-1]:
                flag = 0
                if val&(1<<bit) > 0:
                    flag = 1
                if not cur.child[flag]:
                    cur.child[flag] = Node()
                cur = cur.child[flag]
            return
        def query(val):
            res = 0
            cur = root
            for bit in range(32)[::-1]:
                flag = 0
                if val&(1<<bit) > 0:
                    flag = 1
                if cur.child[1-flag]:
                    res = (res<<1) + 1
                    cur = cur.child[1-flag]
                elif cur.child[flag]:
                    res = (res<<1) + 0
                    cur = cur.child[flag]
                else:
                    return -1
            return res

        for i in idx:
            x, m = queries[i]
            while pos < len(nums) and nums[pos] <= m:
                insert(nums[pos])
                pos += 1
            tmp = query(x)
            ans[i] = tmp
        return ans 


