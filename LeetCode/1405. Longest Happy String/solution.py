class Solution(object):
    def longestDiverseString(self, a, b, c):
        choices = [[a, 'a'], [b, 'b'], [c, 'c']]
        ans = []

        for _ in range(a+b+c):
            choices.sort(reverse=True)
            for i, (x, c) in enumerate(choices):
                if x and ans[-2:] != [c, c]:
                    ans.append(c)
                    choices[i][0] -= 1
                    break
        return "".join(ans)