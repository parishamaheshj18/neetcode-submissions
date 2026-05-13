class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        UseHashmap:
        - count = [0] * 26 ->Key
        - Value - > iterate through each element of strs, update count, 
        if count exists in keys, append to value else add a new key value pair.
        """
        hash_map_anagrams = {}
        # count = [0]*26 
        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char) - ord('a')] +=1
            separator = "-"
            count_str = separator.join(str(i) for i in count)
            if count_str in list(hash_map_anagrams.keys()):
                hash_map_anagrams[count_str].append(word)
            else:
                hash_map_anagrams[count_str] = [word]
        return list(hash_map_anagrams.values())
