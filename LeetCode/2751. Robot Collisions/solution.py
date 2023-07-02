class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        st = []
        idx = list(range(n))
        idx.sort(key = lambda x : positions[x])
        for i in idx:
            if directions[i] == 'L':
                while st and healths[st[-1]] < healths[i]:
                    j = st.pop()
                    healths[j] = -inf
                    healths[i] -= 1
                if st:
                    if healths[st[-1]] == healths[i]:
                        j = st.pop()
                        healths[j] = -inf
                        healths[i] = -inf
                    else:
                        healths[st[-1]] -= 1
                        healths[i] = -inf
            else:
                st.append(i)
        return [healths[i] for i in range(n) if healths[i] != -inf]