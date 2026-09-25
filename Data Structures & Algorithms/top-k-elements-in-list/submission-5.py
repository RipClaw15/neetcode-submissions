class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        for i in nums:
            if f"{i}" in elements:
                elements[f"{i}"]+=1
            else:
                elements[f"{i}"] = 1
        sorted_dict = dict(sorted(elements.items(), key=lambda item: item[1],reverse=True))
        res = list(sorted_dict.keys())[:k]
        return res
