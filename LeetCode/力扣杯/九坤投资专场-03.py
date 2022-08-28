# https://leetcode.cn/contest/ubiquant2022/ranking/

class Solution:
    def minOperations(self, numbers: List[int]) -> int:
        g = numbers[0]
        for x in numbers:
            g = gcd(g,x)
        two, three = [], []
        mx = [0,0]
        for x in numbers:
            x //= g 
            cnt = 0
            while x%2 == 0:
                cnt += 1
                x //= 2
            two.append(cnt)
            mx[0] = max(mx[0],cnt)
            cnt = 0
            while x%3 == 0:
                cnt += 1
                x //= 3
            if x != 1:
                return -1
            three.append(cnt)
            mx[1] = max(mx[1],cnt)
        return sum(mx[0]-two[i]+mx[1]-three[i] for i in range(len(numbers)))

