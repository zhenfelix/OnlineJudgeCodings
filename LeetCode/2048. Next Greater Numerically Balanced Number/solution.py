class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # candidates = [1,22,122,333,1333,4444,14444,22333,55555,155555,224444,122333,1666666,2255555,3334444,1224444]
        # candidates = [1,22,122,333,1333,4444,14444,22333,55555,155555,224444,122333,1224444]
        candidates = [1,22,122,333,1333,4444,14444,22333,55555,155555,224444,122333,666666,1224444]

        nums = []
        for s in candidates:
            ss = set(map(int, [''.join(p) for p in permutations(str(s))]))
            for x in ss:
                nums.append(x)
        nums.sort()
        # print(nums)
        for x in nums:
            if x > n:
                return x 
        return -1




class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        candidates = []
        def dfs(start,target,path,seen):
            if target == 0:
                candidates.append(''.join(str(x)*x for x in path))
                return
            for i in range(start,target+1):
                if i not in seen:
                    seen.add(i)
                    dfs(i+1,target-i,path+[i],seen)
                    seen.remove(i)
            return
        for i in range(1,8):
            dfs(1,i,[],set())
        # print(candidates)
        nums = []
        def my_permute(path, i):
            if i == len(path):
                nums.append(int(''.join(path)))
                return
            for j in range(i,len(path)):
                if j > i and path[j] == path[i]:
                    continue
                path[i], path[j] = path[j], path[i]
                my_permute(path.copy(),i+1)
            return
        for a in candidates:
            my_permute(list(a),0)
        nums.sort()
        # print(nums)
        # assert(len(nums) == len(set(nums)))
        for x in nums:
            if x > n:
                return x

        return -1

