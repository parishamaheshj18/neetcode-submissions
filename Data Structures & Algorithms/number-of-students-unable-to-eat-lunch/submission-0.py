class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt = {}
        cnt[0] = 0
        cnt[1] =0
        for s in students:
            cnt[s]+=1
        for s in sandwiches:
            if cnt[s]>0:
                cnt[s]-=1
                res-=1
            else:
                return res
        return res
