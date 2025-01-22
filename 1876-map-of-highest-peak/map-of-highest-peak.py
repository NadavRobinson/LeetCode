class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:    
        m, n = len(isWater), len(isWater[0])
        height = [[float('inf')] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                else:
                    if i > 0:
                        height[i][j] = min(height[i][j], height[i - 1][j] + 1)
                    if j > 0:
                        height[i][j] = min(height[i][j], height[i][j - 1] + 1)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1:
                    height[i][j] = min(height[i][j], height[i + 1][j] + 1)
                if j < n - 1:
                    height[i][j] = min(height[i][j], height[i][j + 1] + 1)

        return height

        
