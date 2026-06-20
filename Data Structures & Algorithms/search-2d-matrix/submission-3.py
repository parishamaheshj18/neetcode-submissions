class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target<matrix[0][0] or target>matrix[len(matrix)-1][len(matrix[0])-1]:
            return False
        
        rows = len(matrix)
        columns = len(matrix[0])
        up=0
        down=rows-1
        while up <= down:
            m_vert= (up+down)//2

            if matrix[m_vert][-1]< target:
                up=m_vert+1
            elif matrix[m_vert][0]> target:
                down=m_vert-1
            # elif matrix[m_vert][0]== target:
            #     return True
            else:
                l = 0
                r = columns-1
                while l <= r:
                    m_hor = (l+r)//2
                    if matrix[m_vert][m_hor]< target:
                        l = m_hor+1
                    elif matrix[m_vert][m_hor]> target:
                        r=m_hor-1
                    elif matrix[m_vert][m_hor]== target:
                        return True
                return False

        return False