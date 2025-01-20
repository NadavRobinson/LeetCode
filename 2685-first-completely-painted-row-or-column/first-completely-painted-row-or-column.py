class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        cords = {}
        for i in range(m):
            for j in range(n):
                cords[mat[i][j]] = [i,j]
        
        arrRows = [n] * m
        arrCols = [m for i in range(n)]
        
        for i in range(len(arr)):
            row = cords[arr[i]][0]
            col = cords[arr[i]][1]
            if arrRows[row] == 1 or arrCols[col] == 1:
                return i
            arrRows[row] -= 1
            arrCols[col] -= 1
        
