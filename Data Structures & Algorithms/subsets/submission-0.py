class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset  = []
        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            backtrack(i+1)
            # res.append(subset)
            # decision to not include nums[i]
            subset.pop()
            backtrack(i+1)
            # res.append(subset)
            # return res
        backtrack(0)
        return res