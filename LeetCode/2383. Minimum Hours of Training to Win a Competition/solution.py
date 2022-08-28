class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        dex, den = 0, 0
        for ex, en in zip(experience,energy):
            if initialExperience <= ex:
                dex += ex+1-initialExperience
                initialExperience = ex+1
            if initialEnergy <= en:
                den += en+1-initialEnergy
                initialEnergy = en+1 
            initialEnergy -= en 
            initialExperience += ex  
            # print(initialEnergy,initialExperience)
        return dex+den 