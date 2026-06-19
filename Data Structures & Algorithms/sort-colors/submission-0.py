class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for num in nums:
            count[num]+=1
        ptr = 0
        for i in range(len(count)):
            for j in range(count[i]):
                nums[ptr] = i
                ptr+=1
        



        