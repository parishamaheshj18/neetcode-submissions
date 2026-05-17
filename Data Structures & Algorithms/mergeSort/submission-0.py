# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) -1)

    def mergeSortHelper(self,pairs, s, e):
        if e-s+1 <= 1:
            return pairs
        m = (s+e) // 2 # if 5 len - s=0, e = 4, m = 2
        self.mergeSortHelper(pairs, s,m)
        self.mergeSortHelper(pairs,m+1,e)
        self.merge(pairs,s,m,e) # 0, 2, 4

        return pairs

    def merge(self,pairs, s, m, e):
        L = pairs[s:m+1] # 0,1,2
        R = pairs[m+1:e+1] # 3,4

        i = 0 # index L
        j = 0 # index R
        k = s # index pairs

        while i < len(L) and j < len(R): # i<=2,  j<= 2
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i+=1
                k+=1
            else:
                pairs[k] = R[j]
                j+=1
                k+=1
        while j < len(R):
            pairs[k] = R[j]
            j+=1
            k+=1
        while i < len(L):
            pairs[k] = L[i]
            i+=1
            k+=1
        return pairs



        
        # fill with the leftover values


    

