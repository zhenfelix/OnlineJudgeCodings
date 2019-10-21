from collections import Counter
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        cnt, n, right, types = 0, len(tree), 0, 0
        cc = Counter()
        for left in range(n):
            
            while right < n and types <= 2:
                fruit = tree[right]
                if cc[fruit] == 0:
                    cc[fruit] += 1
                    types += 1
                else:
                    cc[fruit] += 1
                if types > 2:
                    cc[fruit] -= 1
                    types -= 1
                    break
                right += 1
            cnt = max(cnt, right-left)
            # print(cc,types,left,right)
            fruit = tree[left]
            cc[fruit] -= 1
            if cc[fruit] == 0:
                types -= 1
        return cnt