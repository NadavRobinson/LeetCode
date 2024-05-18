class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            result = target - nums[i]
            if result in dictionary:
                return [dictionary[result], i]
            dictionary[nums[i]] = i
        
        