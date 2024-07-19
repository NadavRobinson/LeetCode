class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        result = []
        minList = []
        maxList = []
        for row in matrix:
            minList.append(min(row))
        for j in range(len(matrix[0])):
            maxElement = matrix[0][j]
            for i in range(1, len(matrix)):
                if matrix[i][j] > maxElement:
                    maxElement = matrix[i][j]
            maxList.append(maxElement)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == minList[i] and matrix[i][j] == maxList[j]:
                    result.append(matrix[i][j])

        return result
        
                
