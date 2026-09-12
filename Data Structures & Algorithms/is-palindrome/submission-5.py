class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        result = "".join(char for char in s if char.isalpha() or char.isdigit())
        return result == result[::-1]