class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cc = [0,0]
        for x in students:
            cc[x] += 1
        for i, y in enumerate(sandwiches):
            if cc[y] > 0:
                cc[y] -= 1
            else:
                return len(sandwiches)-i 
        return 0