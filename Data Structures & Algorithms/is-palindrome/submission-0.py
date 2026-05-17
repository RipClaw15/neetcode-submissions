class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        s = s.lower()
        for i in s:
            if i in "qwertyuiopasdfghjklzxcvbnm0123456789":
                word += i
        
        if word == word[::-1]:
            return True
        return False