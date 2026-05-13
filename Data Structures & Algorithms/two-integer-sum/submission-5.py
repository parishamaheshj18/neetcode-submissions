class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        q-1) Is the list sorted?
        q-2) What if there are no number that sums up to target.
        Brute Force:
        - One pointer i to iterate from  0 to len(nums).
        - one pointer j to iterate from i to len(nums)
        - [ans1,ans2] -> return array.
        - O(n^2)

        Hashmap:
        - Map Values : index
        - i, T -> check if T-i exists in the hashmap keys



        """
        hash_map = {}
        for i in range(len(nums)):
            num2 = target-nums[i]
            if num2 in hash_map.keys():
                return [i, hash_map[num2]] if i<hash_map[num2] else [hash_map[num2],i]
            else:
                hash_map[nums[i]] = i
        return False

        


        

        