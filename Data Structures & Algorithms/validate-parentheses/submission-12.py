class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        par = {')':'(',']':'[','}':'{'}
        
        newp = []
        for p in s:
            if p in "{[(":
                newp.append(p)
            elif p in "}])":
                if not newp or par[p] != newp.pop():
                    return False
        return not bool(newp)
            