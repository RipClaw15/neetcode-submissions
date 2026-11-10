class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pars = {"{":"}","(":")","[":"]"}

        for p in s:
            if p in "({[":
                stack.append(p)
            elif p in ")}]":
                if stack:
                    if pars[stack.pop()] == p:
                        continue
                    else:
                        return False
                return False
        return not(bool(stack))
        
                        
