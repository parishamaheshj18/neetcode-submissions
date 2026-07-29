class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub_res = []
        res.append(sub_res.copy())
        def backtrack(i):
            
            while i<len(nums):
            
                sub_res.append(nums[i])
                if sub_res not in res:
                    res.append(sub_res.copy())
                backtrack(i+1)

                sub_res.pop()
                backtrack(i+1)
                return res
        
        
        return backtrack(0)


