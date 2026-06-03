class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for p in s:
            if p in "({[":
                res.append(p)
            elif bool(res):
                print(res,p)
                if p == ")" and res[-1] == "(":
                    res.pop()
                elif p == "]" and res[-1] == "[":
                    res.pop()
                elif p == "}" and res[-1] == "{":
                    res.pop()
                else:
                    return False
            else:
                return False
        return not bool(res)