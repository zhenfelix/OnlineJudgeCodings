class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        sums = sum(milestones)
        mx = max(milestones)
        rm = sums - mx
        return min(sums, rm*2+1)
        


Round E 2021 - Kick Start 2021 
Shuffled Anagrams

