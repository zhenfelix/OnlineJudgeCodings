
# class Solution:
#     def isSolvable(self, words: List[str], result: str) -> bool:
#         start, others = set(), set()
#         for word in words + [result]:
#             if len(word) > 1:
#                 start.add(word[0])
#             others |= set(list(word))
#         # for ch in start:
#         #     others.remove(ch)

#         others = list(others)
#         # n = len(others)
#         # def dfs(idx,visited,mp):
#         #     if idx == n:
#         #         return sum(int(''.join(list(map(lambda x:str(mp[x]),list(word))))) for word in words) == int(''.join(list(map(lambda x:str(mp[x]),list(result)))))
#         #     ch = others[idx]
#         #     begin = 0
#         #     if ch in start:
#         #         begin = 1
#         #     for x in range(begin,10):
#         #         if x not in visited:
#         #             visited.add(x)
#         #             mp[ch] = x
#         #             if dfs(idx+1,visited,mp.copy()):
#         #                 return True
#         #             visited.remove(x)
#         #     return False

#         n = max(map(len, words + [result]))
#         if len(result) < n:
#             return False

#         def dfs(idx, i, carry, visited, mp):
#             if idx == n:
#                 return carry == 0
#             if i == len(words) + 1:
#                 sums = sum(mp[word[-idx - 1]] if idx < len(word) else 0 for word in words) + carry
#                 if sums % 10 == mp[result[-idx - 1]]:
#                     carry = sums // 10
#                     return dfs(idx + 1, 0, carry, visited, mp)
#                 return False

#             if (i < len(words) and idx >= len(words[i])):
#                 return dfs(idx, i + 1, carry, visited, mp)
#             tmp = words + [result]
#             ch = tmp[i][-idx-1]
#             if ch in mp:
#                 return dfs(idx, i + 1, carry, visited, mp)
#             begin = 0
#             if ch in start:
#                 begin = 1
#             for x in range(begin, 10):
#                 if x not in visited:
#                     visited.add(x)
#                     mp[ch] = x
#                     if dfs(idx, i + 1, carry, visited, mp.copy()):
#                         return True
#                     visited.remove(x)
#             return False

#         return dfs(0, 0, 0, set(), {})



# class Solution:
#     def isSolvable(self, words: List[str], result: str) -> bool:
#         allWords = words + [result]
#         firstChars = set(word[0] for word in allWords if len(word) > 1)
#         n = max(map(len, allWords))
#         if len(result) < n: return False
#         def dfs(charIdx, wordIdx, carry, visited, char2digit):
#             if charIdx == n: return carry == 0
#             if wordIdx == len(allWords):
#                 # time to check the final status for the current digit
#                 sums = sum(char2digit[word[-charIdx - 1]] if charIdx < len(word) else 0 for word in words) + carry
#                 if sums % 10 == char2digit[result[-charIdx - 1]]:
#                     return dfs(charIdx + 1, 0, sums // 10, visited, char2digit)
#                 else:
#                     return False # prune. To support this, using -charIdx - 1 to visit from right/low to left/high
#             # current word length is too short to check, move to check next word
#             if wordIdx < len(words) and charIdx >= len(words[wordIdx]):
#                 return dfs(charIdx, wordIdx + 1, carry, visited, char2digit)

#             c = allWords[wordIdx][-charIdx-1]
#             if c in char2digit:
#                 # if current word's current char already map to a digit, continue with next word
#                 return dfs(charIdx, wordIdx + 1, carry, visited, char2digit)
#             else:
#                 # otherwise try all possibilities via dfs
#                 firstDigit = 1 if c in firstChars else 0
#                 for digit in range(firstDigit, 10):
#                     if digit not in visited:
#                         visited.add(digit)
#                         char2digit[c] = digit
#                         if dfs(charIdx, wordIdx + 1, carry, visited, char2digit.copy()): return True
#                         visited.remove(digit) # restore visited and char2digit by discarding the copy
#                 return False
#         return dfs(0, 0, 0, set(), {})


class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        allWords = words + [result]
        firstChars = set(word[0] for word in allWords if len(word) > 1)
        n = max(map(len, allWords))
        if len(result) < n: return False
        char2digit = {}
        def dfs(charIdx, wordIdx, carry):
            if charIdx == n: return carry == 0
            if wordIdx == len(allWords):
                # time to check the final status for the current digit
                sums = sum(char2digit[word[-charIdx - 1]] if charIdx < len(word) else 0 for word in words) + carry
                if sums % 10 == char2digit[result[-charIdx - 1]]:
                    return dfs(charIdx + 1, 0, sums // 10)
                else:
                    return False # prune. To support this, using -charIdx - 1 to visit from right/low to left/high
            # current word length is too short to check, move to check next word
            if wordIdx < len(words) and charIdx >= len(words[wordIdx]):
                return dfs(charIdx, wordIdx + 1, carry)

            c = allWords[wordIdx][-charIdx-1]
            if c in char2digit:
                # if current word's current char already map to a digit, continue with next word
                return dfs(charIdx, wordIdx + 1, carry)
            else:
                # otherwise try all possibilities via dfs
                firstDigit = 1 if c in firstChars else 0
                for digit in range(firstDigit, 10):
                    if digit not in char2digit.values():
                        char2digit[c] = digit
                        if dfs(charIdx, wordIdx + 1, carry): return True
                        del char2digit[c]
                return False
        return dfs(0, 0, 0)