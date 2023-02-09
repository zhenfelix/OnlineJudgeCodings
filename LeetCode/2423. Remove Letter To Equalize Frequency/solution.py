class Solution:
    def equalFrequency(self, word: str) -> bool:
        cc = Counter(word)
        arr = [v for k, v in cc.items()]
        n = len(arr)
        for i in range(n):
            arr[i] -= 1
            if len(set([a for a in arr if a])) == 1:
                return True 
            arr[i] += 1
        return False
