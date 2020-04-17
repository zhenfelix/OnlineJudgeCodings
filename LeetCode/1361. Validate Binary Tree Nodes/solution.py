class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        n = len(leftChild)
        counts = [1]*n
        color = [-1]*n

        def dfs(cur):
            color[cur] = 0
            left, right = leftChild[cur], rightChild[cur]
            if left >= 0:
            	if color[left] == 0 or (color[left] == -1 and not dfs(left)):
            		return False
            	counts[cur] += counts[left]
            if right >= 0: 
            	if color[right] == 0 or (color[right] == -1 and not dfs(right)):
            		return False
            	counts[cur] += counts[right]
            color[cur] = 1
            return True

        for i in range(n):
            if color[i] == -1:
                if not dfs(i):
                    return False
      
        # print(counts)
        return max(counts) == n 
        
        

                
                
                
                
                
            
