class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n == 1:
            return [1]
        
        pref = []
        suf = []
        left = 1
        right = n-1
        prod = 1
        while left < right+1:
            prod *= nums[left-1]
            pref.append(prod)
            left += 1
        left = 0
        right = n-2
        prod = 1
        while right > left-1:
            prod *= nums[right+1]
            suf.append(prod)
            right -= 1
        

        res = [0] * n

        res[0] = suf[-1]
        res[-1] = pref[-1]
        
        for i in range(1,n-1):
            res[i] = pref[i-1] * suf[n-2-i]
        return res