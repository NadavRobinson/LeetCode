class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        numOfSteps = 0
        while num > 0:
            numOfSteps += 2 if (num & 1) else 1
            num >>= 1
        return numOfSteps - 1