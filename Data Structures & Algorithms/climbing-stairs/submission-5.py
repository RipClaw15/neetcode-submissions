class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        curr = 1
        for i in range(0,n):
            nxt = curr + prev
            prev = curr
            curr = nxt
             
        return prev
        