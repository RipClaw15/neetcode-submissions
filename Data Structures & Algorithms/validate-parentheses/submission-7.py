class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for p in s:
            if p in "{[(":
                res.append(p)
            else:
                if p == "}":
                    if len(res) == 0:
                        return False
                    if res.pop() == "{":
                        continue
                    else:
                        return False
                elif p == "]":
                    if len(res) == 0:
                        return False
                    if res.pop() == "[":
                        continue
                    else:
                        return False
                elif p == ")":
                    if len(res) == 0:
                        return False
                    if res.pop() == "(":
                        continue
                    else:
                        return False
        if len(res) == 0:
            return True
        return False
                