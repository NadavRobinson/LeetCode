class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        max = 0
        for i in range(len(nums)):
            if i < len(nums) - 2:                
                temp = nums[i] + nums[i+1] + nums[i+2]
                if (temp - nums[i+2] > nums[i+2]) and temp > max:
                    max = temp
        return max            