class Solution:
    def lastMaterial(self, material: List[int]) -> int:
        material = [-m for m in material]
        heapify(material)
        while len(material) > 1:
            a = heappop(material)
            b = heappop(material)
            a -= b
            heappush(material, a)
            # print(material)
        return -material[0]