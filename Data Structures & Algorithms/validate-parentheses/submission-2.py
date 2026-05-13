class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        map = {"{":1, "[":2,"(":3, "}":1, "]":2,")":3}
        for char in s:
            if char in ["{","(","["]:
                brackets.append(map[char])
            elif char in ["}",")","]"]:

                if len(brackets)!=0 and brackets.pop() == map[char]:
                    continue
                else:
                    return False
        if len(brackets) == 0:
            return True
        else:
            return False

        