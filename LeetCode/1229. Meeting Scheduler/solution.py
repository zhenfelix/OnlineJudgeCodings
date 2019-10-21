class Solution:
    # def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
    #     slots = []
    #     for s in slots1:
    #         slots.append((s[0],s[1],1))
    #     for s in slots2:
    #         slots.append((s[0],s[1],2))
    #     slots = sorted(slots)
    #     res = []
    #     for i in range(len(slots)-1):
    #         if slots[i][2] != slots[i+1][2]:
    #             start = max(slots[i][0],slots[i+1][0])
    #             end = min(slots[i][1],slots[i+1][1])
    #             if end - start >= duration:
    #                 res = [start,start+duration]
    #                 break
    #     return res
    
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        s = list(filter(lambda slot: slot[1] - slot[0] >= duration, slots1 + slots2))
        heapq.heapify(s)
        while len(s) > 1:
            cur = heapq.heappop(s)
            if cur[1] >= s[0][0] + duration:
                return [s[0][0], s[0][0] + duration] 
        return []   
            
        