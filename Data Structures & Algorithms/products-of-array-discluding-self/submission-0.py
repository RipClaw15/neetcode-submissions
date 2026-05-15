class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = 1
        zero = 0
        for i in nums:
            if i != 0:
                prod *= i
            else:
                zero += 1
        if zero > 1:
            for i in nums:
                res.append(0)
        elif zero == 1:
            for i in nums:
                if i == 0:
                    res.append(prod)
                else:
                    res.append(0)
        else:
            for i in nums:
                res.append(int(prod/i))
        return res
            
