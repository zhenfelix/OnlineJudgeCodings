class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n = len(receiver)
        tree = [[0]*30 for _ in range(n)]
        parent = [[-1]*30 for _ in range(n)]
        ps = [1]*30
            
        for i in range(n):
            tree[i][0] = receiver[i]  
            parent[i][0] = receiver[i]  
        for p in range(1,30):
            ps[p] = 2*ps[p-1]
            for i in range(n):
                parent[i][p] = parent[parent[i][p-1]][p-1]
                tree[i][p] = tree[i][p-1]+tree[parent[i][p-1]][p-1]

        # print(tree)
        # print(parent)
        # print(ps)

        ans = 0
        for i in range(n):
            s = k 
            j = 29
            cur = i
            while s:
                while j >= 0 and ps[j] > s:
                    j -= 1
                s -= ps[j]
                cur += tree[i][j]
                # print(i,j,parent[i][j])
                i = parent[i][j]
            # print(i,cur)
            ans = max(ans,cur)
        return ans 



class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n = len(receiver)
        # 赋值：初始位置以及起点的得分
        ans = list(range(n))
        pos = list(range(n))
        # 赋值：走 2 ^ 0 步时的结束位置和得分
        ans_2_power = receiver
        pos_2_power = receiver
        for i in range(34):
            if k >> i & 1:
                # 继续往前走 2 ^ i 步
                ans = [ans[i] + ans_2_power[pos[i]] for i in range(n)]
                pos = [pos[pos_2_power[i]] for i in range(n)]
            # 从 2 ^ i 步变成 2 ^ (i + 1) 步
            ans_2_power = [ans_2_power[i] + ans_2_power[pos_2_power[i]] for i in range(n)]
            pos_2_power = [pos_2_power[x] for x in pos_2_power]
        return max(ans)


# 作者：小羊肖恩
# 链接：https://leetcode.cn/circle/discuss/VghzJ4/view/grswHF/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。