class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        m = len(target)
        dictionary = [word for word in dictionary if len(word) == m]

        def match(state, word):
            # if len(word) != m:
            #     return False
            for i in range(m):
                if (state>>i)&1:
                    if target[i] != word[i]:
                        return False
            return True

        @cache
        def calc(state):
            cnt, pre = 0, -1
            for i in range(m):
                cur = (state>>i)&1
                if cur == 1 or cur != pre:
                    cnt += 1
                pre = cur
            return cnt

        def convert(state):
            ans = []
            cnt = 0
            for i in range(m):
                if (state>>i)&1:
                    if cnt > 0:
                        ans.append(str(cnt))
                        cnt = 0
                    ans.append(target[i])
                else:
                    cnt += 1
            if cnt > 0:
                ans.append(str(cnt))
                cnt = 0
            return ans

        candidate = (1<<m)-1
        for s in range(1<<m):
            # print(bin(s),calc(s))
            if calc(s) >= calc(candidate):
                continue
            valid = True
            for word in dictionary:
                if match(s,word):
                    valid = False
                    break
            if valid:
                candidate = s
        return ''.join(convert(candidate))

