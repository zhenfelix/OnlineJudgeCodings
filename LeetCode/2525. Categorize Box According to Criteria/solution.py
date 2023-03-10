class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        dim = [length,width,height]
        s = 0
        if any(d >= 10**4 for d in dim) or length*width*height >= 10**9:
            s |= 1
        if mass >= 100:
            s |= 2
        if s == 3:
            return "Both"
        if s == 0:
            return "Neither"
        if s == 1:
            return "Bulky"
        return "Heavy"