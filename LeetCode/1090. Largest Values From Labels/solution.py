class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        nums=zip(values,labels)
        nums=sorted(nums,key=lambda x:x[0],reverse=True)
        cc={}
        ans=[]
        for x in nums:
            if len(ans)==num_wanted:
                return sum(ans)
            if (x[1] not in cc) or (cc[x[1]]<use_limit):
                ans.append(x[0])
                if x[1] not in cc:
                    cc[x[1]]=1
                else:
                    cc[x[1]]+=1
        return sum(ans)