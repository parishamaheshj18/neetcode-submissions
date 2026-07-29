class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub_res = []

        def backtrack(i):
            if sum(sub_res) == target:
                return res.append(sub_res.copy())
            if sum(sub_res) > target or i>= len(nums):
                return
            
            sub_res.append(nums[i])
            backtrack(i)

            sub_res.pop()
            backtrack(i+1)

            return res

            
        return backtrack(0)


                
                



