class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        """
        Conditions for anagrams:
        - len(s) == len(t)
        - set(s) == set(t)
        - sorted(s) == sorted(t) - O(n)
        """
        # # Easy to understand code
    
        if sorted(s) !=sorted(t):
            return False
        else: 
            return True

        # if len(s) ==len(t) and set_s == set_t and sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False

        # """
        # Make a hash map. 
        # """
        # if len(s) ==len(t):
        #     countS,countT = {},{}
        #     for i in range(len(s)):
        #         countS[s[i]] = 1+ countS.get(s[i],0)
        #         countT[t[i]] = 1+ countT.get(t[i],0)
        #     for key in countS :
        #         if countS[key] != countT.get(key,0):
        #             return False
        #     return True
                


        # else: 
        #     return False


        