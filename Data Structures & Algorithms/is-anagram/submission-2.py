class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        """
        Conditions for anagrams:
        - len(s) == len(t)
        - set(s) == set(t)
        - sorted(s) == sorted(t)
        """
        set_s, set_t = set(list(s)), set(list(t))
        if len(s) ==len(t) and set_s == set_t and sorted(s) == sorted(t):
            return True
        else:
            return False

        