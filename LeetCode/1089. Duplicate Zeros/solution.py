class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        n = len(arr)
        tmp = [0]*n
        i=0
        j=0
        while i<n:
            print(j,i)
            tmp[i]=arr[j]
            if arr[j]==0:
                i+=1
            i+=1
            j+=1
        # print(tmp)
        for i in range(n):
            arr[i]=tmp[i]
        return
        
                
            
            