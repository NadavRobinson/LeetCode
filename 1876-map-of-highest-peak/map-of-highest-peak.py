class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        rows, cols = len(isWater), len(isWater[0])
        height = [[-1] * cols for _ in range(rows)]
        cellQueue = deque()

        for row in range(rows):
            for col in range(cols):
                if isWater[row][col] == 1:
                    height[row][col] = 0
                    cellQueue.append([row, col])
        current_level = 1
        while cellQueue:
            queue_size = len(cellQueue)
            for i in range(queue_size):
                currentCell = cellQueue.popleft()
                for i in range(4):
                    neighborX = currentCell[0] + dx[i]
                    neighborY = currentCell[1] + dy[i]
                    if self.validCell(neighborX, neighborY, rows, cols) and height[neighborX][neighborY] == -1:
                        height[neighborX][neighborY] = current_level
                        cellQueue.append([neighborX, neighborY])
            current_level += 1
    
        return height
    
    def validCell(self, x, y, rows, cols):
        return 0 <= x < rows and 0 <= y < cols

        
